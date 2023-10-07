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
                <span><b-button v-b-modal.modal-4 class="bg-success" @click="updateModal(item)">Edit</b-button></span>
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
            <b-modal id="modal-4" title="Edit Author" @ok="updateAuthor">
                <b-form @submit="updateAuthor">
                    <b-form-group id="input-group-1" label="Author Name:" label-for="input-1">
                        <b-form-input
                            id="input-1"
                            v-model="updateForm.author_name"
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
            // Table Data
            perPage: 3,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'author_name', 'number_of_books', 'actions'],
            authors: [],
            // Form Data
            form: {
                author_name: '',
                number_of_books: 0,
            },
            updateForm: {
                author_name: '',
            },
            filter: null,
            output: null,
        };
    },
    mounted() {
        this.getAuthors();
        this.authors = this.$store.state.authors;
        this.rows = this.authors.length;
    },
    methods: {
        onFiltered(filteredItems) {
            this.rows = filteredItems.length;
            this.currentPage = 1;
        },
        async getAuthors() {
            // const response = await this.$axios.get('/authors');
            // this.$store.commit('ALL_AUTHORS', response.data);
        },
        async updateModal(author) {
            this.updateForm.author_name = author.author_name;
        },
        async updateAuthor() {
            const data = {
                id: author.id,
                author_name: this.updateForm.author_name,
            };
            console.log(data);
            // const response = await this.$axios.update(`/update-author/${data.id}`, data);
            // console.log(response);
        },
        async deteleAuthor(author) {
            const data = {
                id: author.id,
            };
            // const response = await this.$axios.delete(`/delete-author/${data.id}`);
            // console.log(response);
            this.$store.commit('DELETE_AUTHOR', data);
        },
    },
};
</script>
