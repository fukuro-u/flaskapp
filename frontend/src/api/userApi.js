import axios from 'axios';

const baseUrl = 'api/users'; // Change to your backend API URL

export default {
    async getUsers() {
        const response = await axios.get(baseUrl);
        return response.data;
    },
    async addUser(user) {
        const response = await axios.post(baseUrl, user);
        return response.data;
    },
    async updateUser(userId, user) {
        const response = await axios.put(`${baseUrl}/${userId}`, user);
        return response.data;
    },
    async deleteUser(userId) {
        const response = await axios.delete(`${baseUrl}/${userId}`);
        return response.data;
    }
};