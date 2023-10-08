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
                    <b-form-select v-model="form.author" label="author_name">
                        <option v-for="item in authors" :key="item.id" v-bind:value="{ item }">
                            {{ item.author_name }}
                        </option>
                    </b-form-select>
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
                book_name: '',
                number_of_pages: 0,
                author: {},
            },
            authors: [],
        };
    },
    mounted() {
        this.getAuthors();
    },
    methods: {
        async onSubmit(event) {
            event.preventDefault();
            if (this.form.book_name && this.form.author) {
                try {
                    const data = {
                        author_id: this.form.author.item.id,
                        book_name: this.form.book_name,
                        author_name: this.form.author.item.author_name,
                        number_of_pages: this.form.number_of_pages,
                    };
                    const token = localStorage.getItem('access_token');
                    if (token !== undefined) {
                        const response = await this.$axios.post('/add-book', data, {
                            headers: {
                                Authorization: `Bearer ${token}`,
                                Accept: 'multipart/form-data',
                                'Content-Type': 'application/json',
                            },
                        });
                        if ((response.status = 200)) {
                            this.$store.commit('ADD_BOOK', response.data);
                            this.form.book_name = '';
                            this.form.author_name = '';
                            this.form.number_of_pages = 0;
                        } else {
                            this.$router.push({ path: '/' });
                        }
                    } else {
                        this.$router.push({ path: '/' });
                    }
                } catch (error) {
                    console.error(error);
                }
            } else {
                this.show = true;
            }
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
    },
};
</script>

<style></style>
