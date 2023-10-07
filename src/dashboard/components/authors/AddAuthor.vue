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
                id: Math.random(),
                author_name: '',
                number_of_books: 43,
            },
            show: false,
        };
    },
    methods: {
        async onSubmit(event) {
            event.preventDefault();
            if (this.form.author_name === '') {
                this.show = true;
            }
            const data = {
                id: this.form.id,
                author_name: this.form.author_name,
                number_of_books: this.form.number_of_books,
            };
            // const response = await this.$axios.post('/add-author', data);
            // console.log(response);
            this.$store.commit('ADD_AUTHOR', data);
            this.form.author_name = '';
        },
    },
};
</script>

<style></style>
