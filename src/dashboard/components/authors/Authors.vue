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
            // Table Data
            perPage: 3,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'author_name', 'number_of_books', 'actions'],
            authors: [],
            // Form Data
            form: {
                author_id: '',
                author_name: '',
                number_of_books: 0,
            },
            filter: null,
            output: null,
        };
    },
    mounted() {
        this.getAuthors();
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
                if (token !== null) {
                    const response = await this.$axios.get('/authors', {
                        headers: { Authorization: `Bearer ${token}` },
                    });
                    response.data.map(async (item) => {
                        const res = await this.$axios.get(`/author-books/${item.id}`, {
                            headers: { Authorization: `Bearer ${token}` },
                        });
                        item.number_of_books = res.data.length;
                        this.authors.unshift(item);
                        return;
                    });
                    this.rows = response.data.length;
                } else {
                    this.$toast.error('Not Authorized', { duration: 5000 });
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                console.error(error);
            }
        },

        // Function to set initial variables for author during update
        async updateModal(author) {
            this.form.author_id = author.id;
            this.form.author_name = author.author_name;
        },

        // Function to update author
        async updateAuthor() {
            if (this.form.author_name === '') {
                this.$toast.error('Add author name', { duration: 5000 });
                return;
            }
            const data = {
                id: this.form.author_id,
                author_name: this.form.author_name,
            };
            try {
                const token = localStorage.getItem('access_token');
                if (token !== null) {
                    const response = await this.$axios.put(`/update-author`, data, {
                        headers: {
                            Authorization: `Bearer ${token}`,
                            Accept: 'multipart/form-data',
                            'Content-Type': 'application/json',
                        },
                    });
                    if ((response.status = 200)) {
                        this.$toast.success('Author updated', { duration: 5000 });
                        this.form.author_id = '';
                        this.form.author_name = '';
                    } else {
                        this.$toast.error('Not Authorized', { duration: 5000 });
                        this.$router.push({ path: '/' });
                    }
                } else {
                    this.$toast.error('Not Authorized', { duration: 5000 });
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                this.$toast.success('Check all fields', { duration: 5000 });
                console.error(error);
            }
        },

        // Function to delete author
        async deteleAuthor(author) {
            if (confirm('Are you sure to delete author?') === true) {
                const data = {
                    id: author.id,
                };
                try {
                    const token = localStorage.getItem('access_token');
                    if (token !== null) {
                        const response = await this.$axios.delete(`/delete-author`, {
                            headers: {
                                Authorization: `Bearer ${token}`,
                                Accept: 'multipart/form-data',
                                'Content-Type': 'application/json',
                            },
                            data,
                        });
                        if ((response.status = 200)) {
                            this.$toast.success('Author deleted', { duration: 5000 });
                            return true;
                        } else {
                            this.$toast.error('Not Authorized', { duration: 5000 });
                            this.$router.push({ path: '/' });
                        }
                    } else {
                        this.$toast.error('Not Authorized', { duration: 5000 });
                        this.$router.push({ path: '/' });
                    }
                } catch (error) {
                    this.$toast.error('An error occured', { duration: 5000 });
                    console.error(error);
                }
            }
        },
    },
};
</script>
