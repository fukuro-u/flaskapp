<script>
export default {
  props: ['users'],
};
</script>

<template>
  <div class="col-md-6">
    <h2>Users</h2>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>
            <button class="btn btn-warning" @click="$emit('update-user', user)">Update</button>
            <button class="btn btn-danger" @click="$emit('delete-user', user.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>