<template>
    <b-form @submit="onSubmit" v-if="show">
        <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
            <b-form-input id="input-2" v-model="form.name" placeholder="Enter name" required></b-form-input>
        </b-form-group>

        <b-form-group>
            <label for="text-password">Password</label>
            <b-form-input
                type="password"
                v-model="form.password"
                id="text-password"
                placeholder="Enter password"
                required
                aria-describedby="password-help-block"
            ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            form: {
                name: '',
                password: '',
            },

            show: true,
        };
    },
    methods: {
        onSubmit(event) {
            event.preventDefault();
            this.$router.push({ path: 'books' });
        },
    },
};
</script>
