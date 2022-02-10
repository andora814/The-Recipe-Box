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
        search_input: ''
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
        },
        handleDelete(id) {
            this.recipe_array = this.recipe_array.filter(recipe => recipe.id !== id)
        },
        selectRecipe(id) {
            this.$router.push(`/recipedetails/${id}`)
        },
        filterRecipes() {
            // this.filtered_recipes = this.recipe_array.filter(recipe => recipe.recipe_ingredients.includes(this.search_input));
            this.filtered_recipes = this.recipe_array.filter(recipe => recipe.title.includes(this.search_input));
            // how do i search ingredients instead of title?
            // how do i enable user to click on recipe box after searching?
            // how do i search regardless of capitalization?
            this.recipe_array = this.filtered_recipes
            this.search_input = ''
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