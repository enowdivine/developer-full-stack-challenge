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

                    <b-form-group id="input-group-3" label="Author Name:" label-for="input-3">
                        <b-form-select v-model="form.author">
                            <option v-for="item in authors" :key="item.id" v-bind:value="{ item }">
                                {{ item.author_name }}
                            </option>
                        </b-form-select>
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
                </b-form>
            </b-modal>
        </div>
    </div>
</template>

<script>
import AddBook from './AddBook.vue';

export default {
    components: {
        AddBook,
    },
    data() {
        return {
            // Table Data
            perPage: 3,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'book_name', 'author_name', 'number_of_pages', 'actions'],
            books: [],
            filter: null,
            output: null,

            // Form Data
            form: {
                id: '',
                book_name: '',
                number_of_pages: 0,
                author: {},
            },

            // Authors Array
            authors: [],
        };
    },
    mounted() {
        this.getAuthors();
        this.getBooks();
    },
    methods: {
        onFiltered(filteredItems) {
            this.rows = filteredItems.length;
            this.currentPage = 1;
        },

        // Function to get authors from database
        async getAuthors() {
            try {
                const token = localStorage.getItem('access_token');
                if (token !== undefined) {
                    const response = await this.$axios.get('/authors', {
                        headers: { Authorization: `Bearer ${token}` },
                    });
                    this.$store.commit('ALL_AUTHORS', response.data);
                    this.authors = response.data;
                } else {
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                console.error(error);
            }
        },

        // Function to get books from database
        async getBooks() {
            try {
                const token = localStorage.getItem('access_token');
                if (token !== undefined) {
                    const response = await this.$axios.get('/books', {
                        headers: { Authorization: `Bearer ${token}` },
                    });
                    this.$store.commit('ALL_BOOKS', response.data);
                    this.books = response.data;
                    this.rows = response.data.length;
                } else {
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                console.error(error);
            }
        },

        async updateModal(book) {
            this.form.id = book.id;
            this.form.book_name = book.book_name;
            this.form.number_of_pages = book.number_of_pages;
        },
        async updateBook() {
            try {
                const data = {
                    id: this.form.id,
                    book_name: this.form.book_name,
                    number_of_pages: this.form.number_of_pages,
                    author_id: this.form.author.item.id,
                    author_name: this.form.author.item.author_name,
                };
                const token = localStorage.getItem('access_token');
                if (token !== undefined) {
                    const response = await this.$axios.put(`/update-book`, data, {
                        headers: {
                            Authorization: `Bearer ${token}`,
                            Accept: 'multipart/form-data',
                            'Content-Type': 'application/json',
                        },
                    });
                    if ((response.status = 200)) {
                        this.form.id = '';
                        this.form.book_name = '';
                        this.form.number_of_pages = '';
                        this.form.author = {};
                    } else {
                        this.$router.push({ path: '/' });
                    }
                } else {
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                console.error(error);
            }
        },

        // Funtion to delete book
        async deteleBook(book) {
            if (confirm('Are you sure to delete book?') === true) {
                const data = {
                    id: book.id,
                };
                try {
                    const token = localStorage.getItem('access_token');
                    if (token !== undefined) {
                        const response = await this.$axios.delete(`/delete-book`, {
                            headers: {
                                Authorization: `Bearer ${token}`,
                                Accept: 'multipart/form-data',
                                'Content-Type': 'application/json',
                            },
                            data,
                        });
                        if ((response.status = 200)) {
                            return true;
                        } else {
                            this.$router.push({ path: '/' });
                        }
                    } else {
                        this.$router.push({ path: '/' });
                    }
                } catch (error) {
                    console.error(error);
                }
            }
        },
    },
};
</script>
