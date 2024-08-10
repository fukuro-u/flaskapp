<script>
export default {
props: ['updatedUser'],
data() {
    return {};
},
methods: {
    saveUpdatedUser() {
    this.$emit('save-updated-user', this.updatedUser);
    this.$emit('update-user', null); // Clear updatedUser after saving
    }
}
};
</script>

<template>
<div v-if="updatedUser">
    <h2>Update User</h2>
    <form @submit.prevent="saveUpdatedUser">
    <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" class="form-control" id="name" v-model="updatedUser.name">
    </div>
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" id="email" v-model="updatedUser.email">
    </div>
    <button type="submit" class="btn btn-primary">Save</button>
    </form>
</div>
</template>