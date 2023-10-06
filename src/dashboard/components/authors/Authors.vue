<template>
    <div class="container border rounded mt-4 p-4 overflow-auto">
        <div>
            <h4>Authors Table</h4>
        </div>
        <div class="d-flex justify-content-center mb-3">
            <b-form-input v-model="filter" type="search" placeholder="Type to filter data"></b-form-input>
            <!-- Add Author Modal Component -->
            <div class="w-25"><AddAuthor /></div>
        </div>

        <!-- Author Table -->
        <b-table
            id="my-table"
            striped
            :filter="filter"
            @filtered="onFiltered"
            :fields="fields"
            :items="authors"
            :per-page="perPage"
            :current-page="currentPage"
            medium
            class="mt-4"
            ><template v-slot:cell(actions)="{ item }">
                <span><b-button v-b-modal.modal-4 class="bg-success" @click="updateAuthor(item)">Edit</b-button></span>
                <span><b-btn @click="deteleAuthor(item)" class="bg-danger">Delete</b-btn></span>
            </template></b-table
        >

        <!-- Table Pagination -->
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
        ></b-pagination>

        <!-- Edit Author Modal -->
        <div>
            <b-modal id="modal-4" title="Edit Author">
                <b-form @submit="updateAuthor">
                    <b-form-group id="input-group-1" label="Author Name:" label-for="input-1">
                        <b-form-input
                            id="input-1"
                            v-model="form.author_name"
                            placeholder="Enter author name"
                            required
                        ></b-form-input>
                    </b-form-group>
                </b-form>
            </b-modal>
        </div>
    </div>
</template>

<script>
import AddAuthor from './AddAuthor.vue';
export default {
    components: {
        AddAuthor,
    },
    data() {
        return {
            perPage: 3,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'author_name', 'number_of_books', 'actions'],
            authors: [
                { id: 1, author_name: 'Fred', number_of_books: 'Flintstone' },
                { id: 2, author_name: 'Wilma', number_of_books: 'Flintstone' },
                { id: 3, author_name: 'Barney', number_of_books: 'Rubble' },
                { id: 4, author_name: 'Betty', number_of_books: 'Rubble' },
                { id: 5, author_name: 'Pebbles', number_of_books: 'Flintstone' },
                { id: 6, author_name: 'Bamm Bamm', number_of_books: 'Rubble' },
                { id: 7, author_name: 'The Great', number_of_books: 'Gazzoo' },
                { id: 8, author_name: 'Rockhead', number_of_books: 'Slate' },
                { id: 9, author_name: 'Pearl', number_of_books: 'Slaghoople' },
            ],
            form: {
                author_name: '',
                number_of_books: 0,
            },
            filter: null,
            output: null,
        };
    },
    mounted() {
        this.rows = this.authors.length;
    },
    methods: {
        onFiltered(filteredItems) {
            this.rows = filteredItems.length;
            this.currentPage = 1;
        },
        updateAuthor(author) {
            console.log(author);
        },
        deteleAuthor(author) {
            console.log(author);
        },
    },
};
</script>
