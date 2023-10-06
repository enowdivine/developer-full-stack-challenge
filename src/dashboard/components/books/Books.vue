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
                <span><b-button v-b-modal.modal-2 class="bg-success" @click="updateBook(item)">Edit</b-button></span>
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
            <b-modal id="modal-2" title="Edit Book">
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
            perPage: 3,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'book_name', 'author_name', 'number_of_pages', 'actions'],
            books: [
                {
                    id: 1,
                    book_name: 'Fred',
                    author_name: 'Flintstone',
                    number_of_pages: 23,
                },
                { id: 2, book_name: 'Wilma', author_name: 'Flintstone', number_of_pages: 23 },
                { id: 3, book_name: 'Barney', author_name: 'Rubble', number_of_pages: 23 },
                { id: 4, book_name: 'Betty', author_name: 'Rubble', number_of_pages: 23 },
                { id: 5, book_name: 'Pebbles', author_name: 'Flintstone', number_of_pages: 23 },
                { id: 6, book_name: 'Bamm Bamm', author_name: 'Rubble', number_of_pages: 23 },
                { id: 7, book_name: 'The Great', author_name: 'Gazzoo', number_of_pages: 23 },
                { id: 8, book_name: 'Rockhead', author_name: 'Slate', number_of_pages: 23 },
                { id: 9, book_name: 'Pearl', author_name: 'Slaghoople', number_of_pages: 23 },
            ],
            form: {
                book_name: '',
                author_name: '',
                number_of_pages: 0,
            },
            filter: null,
            output: null,
        };
    },
    mounted() {
        this.rows = this.books.length;
    },
    methods: {
        onFiltered(filteredItems) {
            this.rows = filteredItems.length;
            this.currentPage = 1;
        },
        updateBook(book) {
            console.log(book);
        },
        deteleBook(book) {
            console.log(book);
        },
    },
};
</script>
