<template>
    <div class="recipe-container-grid">
        <div v-for="recipe in recipe_array" :key="recipe.id">
            <RecipeCard v-bind:recipe="recipe" />
        </div>
    </div>
</template>

<script>
import RecipeCard from '../components/RecipeCard.vue'
import axios from 'axios'
export default {
    name: 'Home',
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
            console.log("mounted function is working")
            const res = await axios.get(`http://localhost:8000/recipes`)
            console.log(res.data)
            this.recipe_array = res.data
        }
    }
    
}
</script>

<style>

</style>