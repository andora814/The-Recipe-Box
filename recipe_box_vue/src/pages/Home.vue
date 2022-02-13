<template>
    <div class="body">
        <h1>Search your recipe box</h1>
        <div class="search-container">
            <input name="search_input" type="text" v-on:input="handleSearchChange" class="title-field" autocomplete="off"/>
            <button @click="handleHomePageSearch(search_input)" :disabled="search_disabled">🔍</button>
        </div>
    </div>
</template>

<script>
// import axios from 'axios'
export default {
    name: 'Home',
    components: {
    },
    data: () => ({
        search_input: ''
    }),
    mounted() {
        
    },
    props: {
    },
    methods: {
        handleSearchChange(e) {
            this[e.target.name] = e.target.value
        },
        handleHomePageSearch(searched_word) {
            this.$router.push({
                name: `RecipeBox`,
                params: {
                    searched_word: searched_word
                }})
        }
        }
    }
</script>

<style scoped>
.body {
    background-image: url('https://i.imgur.com/AixUJfw.jpg');
    height: 100vh;
    background-repeat: no-repeat;
    background-blend-mode: screen;
    background-size: cover;
    padding: 10px;
}
h1 {
    color: white;
    font-size: 50px;
}
button {
    /* color: white; */
    font-size: 30px;
    cursor: pointer;
    text-decoration: none;
    color: white;
    height: 30px;
    outline: none;
    background-color: transparent;
    margin: 10px;
    padding: 0;
    border: none;
    background: none;
}
input {
    height: 30px;
    width: 300px;
    margin: 10px;
}

</style>