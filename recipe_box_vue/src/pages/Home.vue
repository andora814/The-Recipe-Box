<template>
    <div class="body">
        <h1>Search your recipe box</h1>
    <input placeholder="Enter ingredient" name="search_input" type="text" v-on:input="handleSearchChange" class="title-field" :value="search_input"/>
    <button @click="handleHomePageSearch(search_input)" :disabled="search_disabled">Search</button>
    </div>
</template>

<script>

import axios from 'axios'
export default {
    name: 'Home',
    components: {

    },
    data: () => ({
        search_input: '',
        all_ingredients: []
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
            if(this.all_ingredients.includes(searched_word)) {
                this.$router.push({
                name: `RecipeBox`,
                params: {
                    searched_word: searched_word
                }})
            } else {
                alert(`There are currently no recipes with ${searched_word} as an ingredient. Select "Recipe Box" from the navigation bar to view all exisiting recipes.`)
                this.search_input=""
            }
        },
        async GetAllFood() {
            const response = await axios.get('http://localhost:8000/ingredients/'
            )
            this.all_ingredients =response.data.sort()
        }
    }
}
</script>

<style scoped>
.body {
    background-image: url('https://images.unsplash.com/photo-1558818498-28c1e002b655?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80');
    height: 100vh;
    width: 100vh;
    background-repeat: no-repeat
}
/* .image  {
    width: 500px;
    height: 250px
}
.recipe-container-grid {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
} */
h1 {
    color: white;
}
</style>
 