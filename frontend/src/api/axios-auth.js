import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://localhost:5000/api',
    headers: {
        // 'Content-Type': 'application/json',
        'TEST-Token': {
            toString() {
                return `${localStorage.getItem('token')}`
            }
        }
    }
});

export default instance