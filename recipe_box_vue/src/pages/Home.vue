<template>
    <div>
        <h1>Search your recipe box</h1>
    <input placeholder="Enter ingredient" name="search_input" type="text" v-on:input="handleSearchChange" class="title-field"/>
    <button @click="handleHomePageSearch(search_input)" :disabled="search_disabled">Search</button>
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
.image  {
    width: 500px;
    height: 250px
}
.recipe-container-grid {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
}
</style>
d