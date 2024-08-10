import { createApp } from 'vue';
import App from './MyApp.vue';
import UserList from './components/UserList.vue';
import AddUser from './components/AddUser.vue';
import UpdateUser from './components/UpdateUser.vue';
// import userApi from './api/userApi';

const app = createApp(App);

app.component('UserList', UserList);
app.component('AddUser', AddUser);
app.component('UpdateUser', UpdateUser);

app.mount('#app');