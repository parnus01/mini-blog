<template>
	<div id="app">
		<router-view/>
	</div>
</template>

<script>
	export default {
		created() {
			this.$store.dispatch('auth/autoLogin');
		},
	}
</script>

<style lang="scss">
	@import './assets/css/app.scss';

	#app {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}
</style>
