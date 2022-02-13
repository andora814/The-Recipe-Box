<template>
   <div>
    <input placeholder="Enter ingredient" name="search_input" type="text" v-on:input="handleSearchChange" class="title-field" :value="search_input"/>
    <button @click="filterRecipes(search_input)" :disabled="search_disabled">Search</button>
    <button @click="clearSearch">Clear</button>
    <div v-if="no_results">There are currently no recipes with {{search_input}} as an ingredient.</div>
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
    props: {
        searched_word: String
    },
    data: () => ({
        recipe_array: [],
        filtered_recipes: [],
        search_input: '',
        search_disabled: false,
        original_recipe_array: [],
        no_results: false
    }),
    mounted() {
        this.getRecipes()
    },
    methods: {
        handleSearchChange(e) {
            this[e.target.name] = e.target.value
        },
        async getRecipes() {
            if(this.searched_word) {
                const res = await axios.get(`http://localhost:8000/recipes`)
                this.recipe_array = res.data
                this.original_recipe_array = res.data
                this.filterRecipes(this.searched_word)
                this.search_input=this.searched_word
            } else {
            const res = await axios.get(`http://localhost:8000/recipes`)
            this.recipe_array = res.data
            this.original_recipe_array = res.data
            }
        },
        handleDelete(id) {
            this.recipe_array = this.recipe_array.filter(recipe => recipe.id !== id)
        },
        selectRecipe(id) {
            this.$router.push(`/recipedetails/${id}`)
        },
        filterRecipes(search_input) {
            this.search_disabled = true
            let array = []
            if(search_input.length>0) {
            for (let i=0; i<this.recipe_array.length; i++) {
                for(let j=0; j<this.recipe_array[i].recipe_ingredients.length; j++) {
                    if(this.recipe_array[i].recipe_ingredients[j].name.toLowerCase().includes(search_input.toLowerCase())) {
                        array.push(this.recipe_array[i])
                    }
                }
                }
            if(array.length==0) {this.no_results=true} else {this.no_results=false}
            this.filtered_recipes = array
            this.recipe_array = this.filtered_recipes
            this.search_input=''
            } else {
                this.search_disabled = false
            }
            },
        clearSearch() {
            this.search_input = ''
            this.search_disabled = false
            this.recipe_array = this.original_recipe_array
            this.filtered_recipes = []
            this.no_results = false
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