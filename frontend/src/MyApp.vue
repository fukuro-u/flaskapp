<script>
import userApi from './api/userApi';
// import UserList from './components/UserList.vue';
// import AddUser from './components/AddUser.vue';
// import UpdateUser from './components/UpdateUser.vue';

export default {
    data() {
        return {
            users: [],
            updatedUser: null
        };
    },
    mounted() {
        this.getUsers();
    },
    methods: {
        async getUsers() {
            try {
                this.users = await userApi.getUsers();
            } catch (error) {
                console.error(error);
            }
        },
        updateUser(user) {
            this.updatedUser = user;
        },
        async saveUpdatedUser(user) {
            try {
                await userApi.updateUser(user.id, user);
                this.updatedUser = null; // Clear after saving
                this.getUsers();
            } catch (error) {
                console.error(error);
            }
        },
        cancelUpdate() {
            this.updatedUser = null;
        },
        async deleteUser(userId) {
            try {
                await userApi.deleteUser(userId);
                this.getUsers();
            } catch (error) {
                console.error(error);
            }
        }
    }
};
</script>

<template>
    <div>
        <h1>User Management</h1>
        <div class="row">
            <AddUser @user-added="getUsers" />
            <UserList :users="users" @update-user="updateUser" @delete-user="deleteUser" />
            <UpdateUser v-if="updatedUser" :user="updatedUser" @save-updated-user="saveUpdatedUser"
                @cancel-update="cancelUpdate" />
        </div>
    </div>
</template>