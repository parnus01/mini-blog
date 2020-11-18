<template>
    <div class="root">
        <b-navbar toggleable="lg" type="dark" variant="dark">
            <b-navbar-brand href="#">Welcome</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="#">
                        <b-avatar class="mr-3"></b-avatar>
                        <span class="mr-auto">{{ loginName }}</span>
                    </b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item>
                        <b-button class="my-2 my-sm-0" size="sm" type="submit"
                                  @click="logout">Logout
                        </b-button>
                    </b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
        <div class="blog-container clear">
            <b-button variant="outline-primary" class="mb-2 add-btn" @click="openCreateModal">
                Add new blog
                <b-icon icon="plus-circle" aria-hidden="true"></b-icon>
            </b-button>
            <b-list-group v-if="blogs.length > 0">
                <b-list-group-item :key="key" class="flex-column align-items-start"
                                   v-for="(blog,key) in blogs">
                    <div class="d-flex w-100 justify-content-between">
                        <h3 class="mb-1">{{ blog.name}}</h3>
                        <div class="author">{{ blog.author }} <br>
                            <b-badge :variant="mappingVarient(blog.status)" class="status">{{
                                mappingStatus(blog.status)}}
                            </b-badge>
                        </div>
                    </div>
                    <p class="mb-1 mt-4">
                        {{ blog.content }}
                    </p>
                    <div class="category mt-3">
                        <div class="text-right">
                            <b-button variant="primary">
                                #{{ blog.category }}
                            </b-button>
                        </div>
                    </div>
                    <div class="action-container">
                        <b-icon icon="pencil-square" font-scale="2" @click="editBlog(blog.id)"></b-icon>
                        <b-icon icon="trash-fill" variant="danger" font-scale="2" @click="deleteBlog(blog.id)"></b-icon>
                    </div>
                </b-list-group-item>
            </b-list-group>
            <b-modal v-model="modalCreateBlog" @ok="handleOk">

                <b-form ref="form" @submit.stop.prevent="handleSubmit">
                    <b-form-group id="input-group-1" label="Name:" label-for="input-2">
                        <b-form-input
                                id="input-2"
                                v-model="form.name"
                                required
                                placeholder="Enter name"
                        ></b-form-input>
                    </b-form-group>
                    <b-form-group id="input-group-2" label="Content:" label-for="input-2">
                        <b-form-input
                                id="input-2"
                                v-model="form.content"
                                required
                                placeholder="Enter content"
                        ></b-form-input>
                    </b-form-group>
                    <b-form-group id="input-group-3" label="Category:" label-for="input-2">
                        <b-form-input
                                id="input-2"
                                v-model="form.category"
                                required
                                placeholder="Enter category"
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-group-4" label="Status:" label-for="input-3">
                        <b-form-select
                                id="input-3"
                                v-model="form.status"
                                :options="status_list"
                                required
                        ></b-form-select>
                    </b-form-group>
                </b-form>
            </b-modal>
        </div>

    </div>

</template>

<script>
    import axiosAuth from '@/api/axios-auth'

    export default {
        data: function () {
            return {
                form: {
                    mode: '',
                    id: null,
                    name: '',
                    content: '',
                    category: '',
                    status: null
                },
                status_list: [{text: 'Active', value: 1}, {text: 'Inactive', value: 0}],
                modalCreateBlog: false,
                blogs: []
            }
        },
        created() {
            this.fetchBlog()
        },
        computed: {
            loginName() {
                return localStorage.getItem('username')
            }
        },
        methods: {
            logout() {
                this.$store.dispatch('auth/logout')
            },
            fetchBlog() {
                axiosAuth.get('/blog').then(({data}) => {
                    this.blogs = data.blogs
                })
            },
            mappingStatus(status) {
                return (status === 1) ? 'active' : 'inactive'
            },
            mappingVarient(status) {
                return (status === 1) ? 'success' : 'danger'
            },
            openCreateModal() {
                this.clearForm()
                this.form.mode = 'new'
                this.modalCreateBlog = true
            },
            handleSubmit() {
                if (!this.$refs.form.checkValidity()) {
                    return
                }

                if (this.form.mode === 'new') {
                    axiosAuth.post('/blog', this.form).then(({data}) => {
                        if (data.success === true) {
                            this.makeToast('create blog successful', 'success')
                            this.clearForm()
                            this.fetchBlog()
                        }
                    }).catch(() => {
                        this.makeToast('server error', 'danger')
                    }).finally(() => {
                        this.modalCreateBlog = false
                    })
                } else if (this.form.mode === 'edit') {
                    axiosAuth.put(`/blog/${this.form.id}`, this.form).then(() => {
                        this.makeToast('update blog successful', 'success')
                        this.fetchBlog()
                    }).catch(() => {
                        this.makeToast('Permission denied', 'warning')
                    })
                }

            },
            handleOk(e) {
                e.preventDefault()
                this.handleSubmit()
            },
            makeToast(text, variant = null) {
                this.$bvToast.toast(text, {
                    title: 'Notification',
                    variant: variant,
                    solid: true
                })
            },
            clearForm() {
                this.form.id = null
                this.form.name = ''
                this.form.content = ''
                this.form.category = ''
                this.form.status = null
            },
            deleteBlog(id) {
                this.$bvModal.msgBoxConfirm('Are you sure?')
                    .then(value => {
                        if (value) {
                            axiosAuth.delete(`/blog/${id}`).then(({data}) => {
                                this.makeToast('delete blog successful', 'success')
                                this.fetchBlog()
                            }).catch(() => {
                                this.makeToast('Permission denied', 'warning')
                            })
                        }
                    })
            },
            editBlog(id) {
                let blog = this.blogs.find(blog => blog.id === id)
                this.form.id = id
                this.form.mode = 'edit'
                this.form.name = blog.name
                this.form.content = blog.content
                this.form.category = blog.category
                this.form.status = blog.status
                this.modalCreateBlog = true
            }
        }

    }
</script>
<style scoped>
    .blog-container {
        margin: 3% auto;
        width: 80%;
    }

    .author {
        font-weight: bold;
        font-size: 18px;
    }

    .status {
        font-size: 14px;
    }

    .action-container {
        float: left;
    }

    .b-icon {
        margin: 0 10px;
    }

    .add-btn {
        display: table;
    }

</style>