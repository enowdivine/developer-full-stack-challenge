<template>
    <div>
        <b-button v-b-modal.modal-1 class="bg-primary ml-2 w-100">Add Book</b-button>

        <b-modal id="modal-1" title="Add New Book" @ok="onSubmit">
            <b-form @submit="onSubmit">
                <b-form-group id="input-group-1" label="Book Name:" label-for="input-1">
                    <b-form-input
                        id="input-1"
                        v-model="form.book_name"
                        placeholder="Enter book name"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-3" label="Author Name:" label-for="input-3">
                    <b-form-select v-model="form.author_name" :options="authors"></b-form-select>
                </b-form-group>

                <b-form-group id="input-group-4" label="Number of pages:" label-for="input-4">
                    <b-form-input
                        type="number"
                        id="input-4"
                        v-model="form.number_of_pages"
                        placeholder="Enter number of pages"
                        required
                    ></b-form-input>
                </b-form-group>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'AddBook',
    data() {
        return {
            form: {
                id: Math.random(),
                book_name: '',
                author_name: '',
                number_of_pages: 0,
            },
            authors: [],
        };
    },
    mounted() {
        const allAuthors = this.$store.state.authors;
        allAuthors.map((item) => this.authors.push(item.author_name));
    },
    methods: {
        async onSubmit(event) {
            event.preventDefault();
            if (this.form.book_name && this.form.author_name && this.form.number_of_pages) {
                const data = {
                    id: this.form.id,
                    book_name: this.form.book_name,
                    author_name: this.form.author_name,
                    number_of_pages: this.form.number_of_pages,
                };
                // const response = await this.$axios.post('/add-book', data);
                // console.log(response);
                this.$store.commit('ADD_BOOK', data);
                this.form.book_name = '';
                this.form.author_name = '';
                this.form.number_of_pages = '';
            } else {
                this.show = true;
            }
        },
    },
};
</script>

<style></style>
