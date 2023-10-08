<template>
    <div>
        <b-button ref="Btn" v-b-modal.modal-3 class="bg-primary ml-2 w-100">Add Author</b-button>

        <b-modal id="modal-3" title="Add Author" @ok="onSubmit">
            <b-form @submit="onSubmit">
                <b-form-group id="input-group-1" label="Author Name:" label-for="input-1">
                    <b-form-input
                        id="input-1"
                        v-model="form.author_name"
                        placeholder="Enter author name"
                        required
                    ></b-form-input>
                </b-form-group>
            </b-form>
            <div v-if="show">
                <p class="text-danger">Author name is required*</p>
            </div>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'AddAuthor',
    data() {
        return {
            form: {
                author_name: '',
                number_of_books: 0,
            },
            show: false,
        };
    },
    methods: {
        async onSubmit(event) {
            event.preventDefault();
            if (this.form.author_name === '') {
                this.show = true;
                return;
            }
            const data = {
                author_name: this.form.author_name,
                number_of_books: this.form.number_of_books,
            };
            try {
                const token = localStorage.getItem('access_token');
                if (token !== null) {
                    const response = await this.$axios.post('/add-author', data, {
                        headers: {
                            Authorization: `Bearer ${token}`,
                            Accept: 'multipart/form-data',
                            'Content-Type': 'application/json',
                        },
                    });
                    if ((response.status = 200)) {
                        this.$toast.success('Author added', { duration: 5000 });
                        this.form.author_name = '';
                        this.form.number_of_books = 0;
                    }
                } else {
                    this.$toast.error('Not Authorized', { duration: 5000 });
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                this.$toast.error('Check all fields', { duration: 5000 });
                console.error(error);
            }
        },
    },
};
</script>

<style></style>
