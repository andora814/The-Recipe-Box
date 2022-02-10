<template>
    <div id="recipeform">
        <div class="form-container">
            <form @submit="handleSubmit" v-if="show_recipe">
                <div class="flex">
                    <h3>Add a new recipe</h3>
                    <div class="title-minutes-servings-section">
                        <input placeholder="Title" name="title" type="recipe_title" v-on:input="handleFormChange" class="title-field"/>
                        <input placeholder="Total minutes" name="ready_in_minutes" type="ready_in_minutes" v-on:input="handleFormChange" class="integer-field"/>
                        <input placeholder="# of Servings" name="servings" type="servings" v-on:input="handleFormChange" class="integer-field"/>
                    </div>
                    <input placeholder="Image URL" name="image" type="image_url" v-on:input="handleFormChange"/>
                    <input placeholder="Summary" name="summary" type="summary" v-on:input="handleFormChange" class="summary"/>
                    <input placeholder="Instructions" name="instructions" type="instructions" v-on:input="handleFormChange" class="instructions"/>
                    <button class="btn" type="submit">Next</button>
                </div>
            </form>
            <div v-if="show_ingredients" class="flex">
                    <h3>Add ingredients</h3>
                    <ul>
                        <li v-for="ingredient in ingredient_list" :key="ingredient.id">
                            {{ ingredient.quantity}} {{ingredient.unit}} of {{ ingredient.ingredient }}
                        </li>
                    </ul>
                    <div class="ingredient-section">
                        <input placeholder="Ingredient" name="ingredient" type="ingredient" v-on:input="handleFormChange" class="ingredient"/>
                        <input placeholder="Quantity" name="quantity" type="quantity" v-on:input="handleFormChange" class="quantity"/>
                        <input placeholder="Unit" name="unit" type="unit" v-on:input="handleFormChange" class="unit"/>
                        <button @click="addIngredient">+</button>
                    </div>
                    <div class="ingredient-section">
                        <input placeholder="Ingredient" name="ingredient" type="ingredient" v-on:input="handleFormChange" class="ingredient"/>
                        <input placeholder="Quantity" name="quantity" type="quantity" v-on:input="handleFormChange" class="quantity"/>
                        <input placeholder="Unit" name="unit" type="unit" v-on:input="handleFormChange" class="unit"/>
                        <button @click="addIngredient">+</button>
                    </div>
                    <div class="ingredient-section">
                        <input placeholder="Ingredient" name="ingredient" type="ingredient" v-on:input="handleFormChange" class="ingredient"/>
                        <input placeholder="Quantity" name="quantity" type="quantity" v-on:input="handleFormChange" class="quantity"/>
                        <input placeholder="Unit" name="unit" type="unit" v-on:input="handleFormChange" class="unit"/>
                        <button @click="addIngredient">+</button>
                    </div>
                    <div class="ingredient-section">
                        <input placeholder="Ingredient" name="ingredient" type="ingredient" v-on:input="handleFormChange" class="ingredient"/>
                        <input placeholder="Quantity" name="quantity" type="quantity" v-on:input="handleFormChange" class="quantity"/>
                        <input placeholder="Unit" name="unit" type="unit" v-on:input="handleFormChange" class="unit"/>
                        <button @click="addIngredient">+</button>
                    </div>
                    <div class="ingredient-section">
                        <input placeholder="Ingredient" name="ingredient" type="ingredient" v-on:input="handleFormChange" class="ingredient"/>
                        <input placeholder="Quantity" name="quantity" type="quantity" v-on:input="handleFormChange" class="quantity"/>
                        <input placeholder="Unit" name="unit" type="unit" v-on:input="handleFormChange" class="unit"/>
                        <button @click="addIngredient">+</button>
                    </div>
                    <button>Add recipe card!</button>
            </div>
        </div>

    </div>

</template>

<script>
import axios from 'axios'
export default {
    name: 'AddRecipe',
    data: () => ({
        title: '',
        ready_in_minutes: 0,
        servings: 0,
        source_url: '',
        image: '',
        summary: '',
        instructions: '',
        ingredient: '',
        quantity: 0,
        unit: '',
        new_recipe: {},
        new_ingredient: {},
        show_recipe: true,
        show_ingredients: false,
        ingredient_list: [],

    }),
    methods: {
        handleFormChange(e) {
            this[e.target.name] = e.target.value
        },
        async handleSubmit(e) {
            e.preventDefault()
            const recipe_response = await axios.post(`http://localhost:8000/recipes/`, {
                "title": this.title,
                "ready_in_minutes": this.ready_in_minutes,
                "servings": this.servings,
                "source_url": this.source_url,
                "image": this.image,
                "summary": this.summary,
                "instructions": this.instructions
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
            // this.$router.push(`/recipes/${recipe_response.data.id}`)
            this.new_recipe=recipe_response.data
            this.show_recipe = false
            this.show_ingredients = true
        },
        async addIngredient() {
            this.ingredient_list.push({
                "ingredient": this.ingredient,
                "quantity": this.quantity,
                "unit": this.unit
            })
            console.log(this.ingredient_list)
            const ingredient_response = await axios.post(`http://localhost:8000/ingredients/`, {
                "name": this.ingredient,
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
            this.new_ingredient=ingredient_response.data
            await axios.post(`http://localhost:8000/recipeingredients/`, {
                "recipe_id": this.new_recipe.id,
                "ingredient_id": this.new_ingredient.id,
                "name": this.new_ingredient.name,
                "quantity": this.quantity,
                "unit": this.unit,
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
        },

    }
}



</script>

<style scoped>
    h3 {
        color: green;
    }
    input {
        width: 500px;
        height: 30px;
        margin: 10px;    
    }
    .flex {
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .btn {
        width: 509px;
        margin: 10px; 
    }
    .integer-field, .quantity, .unit {
        width: 100px;
        height: 30px;
        margin: 10px;
    }
    .title-field, .ingredient {
        width: 240px;
        height: 30px;
        margin: 10px;
    }
    .title-minutes-servings-section, .ingredient-section {
        display: flex;
    }

    .instructions {
        width: 500px;
        height: 200px;
        margin: 10px;  
    }
</style>