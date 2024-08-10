<script>
import userApi from '../api/userApi';

export default {
  data() {
    return {
      newUser: {
        name: '',
        email: ''
      }
    };
  },
  methods: {
    async addUser() {
      try {
        await userApi.addUser(this.newUser);
        this.newUser.name = '';
        this.newUser.email = '';
        this.$emit('user-added'); // Trigger event to update user list
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<template>
  <div>
    <form @submit.prevent="addUser">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="newUser.name">
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="newUser.email">
      </div>
      <button type="submit">Add User</button>
    </form>
  </div>
</template>