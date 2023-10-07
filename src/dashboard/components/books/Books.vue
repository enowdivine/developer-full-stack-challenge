<template>
    <div class="container border rounded mt-4 p-4 overflow-auto">
        <div>
            <h4>Books Table</h4>
        </div>
        <div class="d-flex justify-content-center mb-3">
            <b-form-input v-model="filter" type="search" placeholder="Type to filter data"></b-form-input>
            <!-- Add Book Modal Component -->
            <div class="w-25"><AddBook /></div>
        </div>

        <!-- Book Table -->
        <b-table
            id="my-table"
            striped
            :filter="filter"
            @filtered="onFiltered"
            :fields="fields"
            :items="books"
            :per-page="perPage"
            :current-page="currentPage"
            medium
            class="mt-4"
            ><template v-slot:cell(actions)="{ item }">
                <span><b-button v-b-modal.modal-2 class="bg-success" @click="updateModal(item)">Edit</b-button></span>
                <span><b-btn @click="deteleBook(item)" class="bg-danger">Delete</b-btn></span>
            </template></b-table
        >

        <!-- Table Pagination -->
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
        ></b-pagination>

        <!-- Edit Book Modal -->
        <div>
            <b-modal id="modal-2" title="Edit Book" @ok="updateBook">
                <b-form @submit="updateBook">
                    <b-form-group id="input-group-1" label="Book Name:" label-for="input-1">
                        <b-form-input
                            id="input-1"
                            v-model="form.book_name"
                            placeholder="Enter book name"
                            required
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-group-2" label="Author Name:" label-for="input-2">
                        <b-form-input
                            id="input-2"
                            v-model="form.author_name"
                            placeholder="Enter author name"
                            required
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-group-3" label="Number of pages:" label-for="input-3">
                        <b-form-input
                            type="number"
                            id="input-3"
                            v-model="form.number_of_pages"
                            placeholder="Enter number of pages"
                            required
                        ></b-form-input>
                    </b-form-group>

                    <!-- <b-button type="submit" variant="primary">Submit</b-button> -->
                </b-form>
            </b-modal>
        </div>
    </div>
</template>

<script>
import AddBook from './AddBook.vue';
import EditBook from './EditBook.vue';

export default {
    components: {
        AddBook,
        EditBook,
    },
    data() {
        return {
            // Table Data
            perPage: 3,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'book_name', 'author_name', 'number_of_pages', 'actions'],
            books: [],
            // Form Data
            form: {
                id: '',
                book_name: '',
                author_name: '',
                number_of_pages: 0,
            },
            filter: null,
            output: null,
        };
    },
    mounted() {
        this.getBooks();
        this.books = this.$store.state.books;
        this.rows = this.books.length;
    },
    methods: {
        onFiltered(filteredItems) {
            this.rows = filteredItems.length;
            this.currentPage = 1;
        },
        async getBooks() {
            // const response = await this.$axios.get('/books');
            // this.$store.commit('ALL_BOOKS', response.data);
        },
        async updateModal(book) {
            this.form.id = book.id;
            this.form.book_name = book.book_name;
            this.form.author_name = book.author_name;
            this.form.number_of_pages = book.number_of_pages;
        },
        async updateBook() {
            const data = {
                id: this.form.id,
                book_name: this.form.book_name,
                author_name: this.form.author_name,
                number_of_pages: this.form.number_of_pages,
            };
            console.log(data);
            // const response = await this.$axios.update(`/update-author/${data.id}`, data);
            // console.log(response);
        },
        deteleBook(book) {
            const data = {
                id: book.id,
            };
            // const response = await this.$axios.delete(`/delete-book/${data.id}`);
            // console.log(response);
            this.$store.commit('DELETE_BOOK', data);
        },
    },
};
</script>
