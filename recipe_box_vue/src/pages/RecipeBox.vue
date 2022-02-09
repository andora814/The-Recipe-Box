<template>
    <div class="recipe-container-grid">
        <div v-for="recipe in recipe_array" :key="recipe.id">
            <RecipeCard v-bind:recipe="recipe" @handleDelete="handleDelete" @click="selectRecipe(recipe.id)"/>
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
        recipe_array: []
    }),
    mounted() {
        this.getRecipes()
    },
    methods: {
        async getRecipes() {
            const res = await axios.get(`http://localhost:8000/recipes`)
            this.recipe_array = res.data
        },
        handleDelete(id) {
            this.recipe_array = this.recipe_array.filter(recipe => recipe.id !== id)
        },
        selectRecipe(id) {
            this.$router.push(`/recipedetails/${id}`)
        }
    }
    
}
</script>

<style scoped>

</style>