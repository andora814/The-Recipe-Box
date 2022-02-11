<template>
   <div>
    <input placeholder="Enter food name" name="search_input" type="text" v-on:input="handleSearchChange" class="title-field"/>
    <button @click="filterRecipes">Search Recipe Box</button>
    <!-- <button @click="clearSearch">Clear Search</button> -->
    <div class="recipe-container-grid">
        <div v-for="recipe in recipe_array" :key="recipe.id">
            <RecipeCard v-bind:recipe="recipe" @handleDelete="handleDelete" @click="selectRecipe(recipe.id)"/>
        </div>
    </div>
    </div>
</template>

<script>
import RecipeCard from '../components/RecipeCard.vue'
import axios from 'axios'
export default {
    name: 'RecipeBox',
    components: {
        RecipeCard
    },
    data: () => ({
        recipe_array: [],
        filtered_recipes: [],
        search_input: '',
        full_list_of_recipes: []
    }),
    mounted() {
        this.getRecipes()
    },
    methods: {
        handleSearchChange(e) {
            this[e.target.name] = e.target.value
        },
        async getRecipes() {
            const res = await axios.get(`http://localhost:8000/recipes`)
            this.recipe_array = res.data
            this.full_list_of_recipes = res.data
        },
        handleDelete(id) {
            this.recipe_array = this.recipe_array.filter(recipe => recipe.id !== id)
        },
        selectRecipe(id) {
            this.$router.push(`/recipedetails/${id}`)
        },
        filterRecipes() {
            let array = []
            for (let i=0; i<this.recipe_array.length; i++) {
                for(let j=0; j<this.recipe_array[i].recipe_ingredients.length; j++) {
                    if(this.recipe_array[i].recipe_ingredients[j].name.toLowerCase().includes(this.search_input.toLowerCase())) {
                        array.push(this.recipe_array[i])
                    }
                }
                }
            this.filtered_recipes = array
            this.recipe_array = this.filtered_recipes
            // this.search_input = ''
            }
        // clearSearch() {
        //     this.search_input = ''
        //     this.$forceUpdate()
        // }
        }
    }
            // this.filtered_recipes = this.recipe_array.filter(recipe => recipe.title.includes(this.search_input));
            // TO DO:
            // Search ingredients instead of title
            // Enable user to click on recipe box after searching
            // Search regardless of capitalization
    

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