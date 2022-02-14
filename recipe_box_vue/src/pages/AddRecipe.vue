<template>
    <div class="body">
        <div class="form-container">
            <form @submit="handleSubmit" v-if="show_recipe">
                <div class="flex">
                    <h3>Add a new recipe</h3>
                    <div class="title-minutes-servings-section">
                        <input placeholder="Title" name="title" type="recipe_title" v-on:input="handleFormChange" class="title-field" autocomplete="off"/>
                        <input placeholder="Total minutes" name="ready_in_minutes" type="ready_in_minutes" v-on:input="handleFormChange" class="integer-field" autocomplete="off"/>
                        <input placeholder="# of Servings" name="servings" type="servings" v-on:input="handleFormChange" class="integer-field" autocomplete="off"/>
                    </div>
                    <input placeholder="Image URL" name="image" type="image_url" v-on:input="handleFormChange" autocomplete="off"/>
                    <input placeholder="Summary" name="summary" type="summary" v-on:input="handleFormChange" class="summary" autocomplete="off"/>
                    <input placeholder="Instructions" name="instructions" type="instructions" v-on:input="handleFormChange" class="instructions" autocomplete="off"/>
                    <button type="submit">Next</button>
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
                        <input placeholder="Ingredient" name="ingredient" type="ingredient" v-on:input="handleIngredientFormChange" class="ingredient" :value="ingredient" autocomplete="off"/>
                        <input placeholder="Quantity" name="quantity" type="quantity" v-on:input="handleFormChange" class="quantity" :value="quantity" autocomplete="off"/>
                        <input placeholder="Unit" name="unit" type="unit" v-on:input="handleFormChange" class="unit" :value="unit" autocomplete="off"/>
                        <button @click="addIngredient(ingredient)">Add ingredient to recipe</button>
                    </div>
                    <div v-if="show_pantry_search" class="suggestions-container">
                        <div>Select pantry ingredient:</div>
                        <div v-for="pantry_item in pantry" :key="pantry_item.id" class="suggestions">
                            <div @click="SelectPantryItem(pantry_item.name)"> {{ pantry_item.name }} </div>
                        </div>
                    </div>
                    <button @click="selectRecipe(new_recipe.id)">Submit</button>
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
        pantry: [],
        show_pantry_search: false,
        filtered_pantry: [],
        panty_item_selected: 0
    }),
    methods: {
        handleFormChange(e) {
            this[e.target.name] = e.target.value
        },
        handleIngredientFormChange(e) {
            this[e.target.name] = e.target.value
            if(e.target.value.length >= 3) {
                this.PantrySearch(this.ingredient)
            }
        },
        async PantrySearch(keyword) {
            console.log(keyword)
            let array = []
            this.show_pantry_search = true
            const response = await axios.get('http://localhost:8000/ingredients/')
            this.pantry = response.data
            for (let i=0; i<this.pantry.length; i++) {
                    if(this.pantry[i].name.toLowerCase().includes(keyword.toLowerCase())) {
                        array.push(this.pantry[i])
                }
                }
            this.filtered_pantry = array
            this.pantry = this.filtered_pantry
        },
        SelectPantryItem(pantry_item) {
            this.ingredient = pantry_item
            this.show_pantry_search=false
            this.pantry_item_selected=true
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
            this.new_recipe=recipe_response.data
            this.show_recipe = false
            this.show_ingredients = true
        },
        async addIngredient(ingredient) {
            console.log("add ingredient is being called")
            if(this.pantry_item_selected) {
            for (let i=0; i<this.pantry.length; i++) {
                if(this.pantry[i].name.toLowerCase()==ingredient.toLowerCase()) {
                this.ingredient_list.push({
                "ingredient": this.ingredient,
                "quantity": this.quantity,
                "unit": this.unit
            })
            await axios.post(`http://localhost:8000/recipeingredients/`, {
                "recipe_id": this.new_recipe.id,
                "ingredient_id": this.pantry[i].id,
                "name": this.pantry[i].name,
                "quantity": this.quantity,
                "unit": this.unit,
            }, {
                auth: {
                    username: 'recipeboxuser',
                    password: 'recipe'
                }
            })
            this.ingredient=""
            this.quantity=""
            this.unit=""
            } else { 
            console.log("first else")}}
            } else { 
            this.ingredient_list.push({
                "ingredient": this.ingredient,
                "quantity": this.quantity,
                "unit": this.unit
            })
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
            this.ingredient=""
            this.quantity=""
            this.unit=""
            }
            
        },
        selectRecipe(id) {
            this.$router.push(`/recipedetails/${id}`)
        },
    }
}
</script>

<style scoped>
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
    button {
        height: 30px;
        margin: 10px;
        outline-style: solid;
        outline-color: white;
        background-color: transparent;
        border: none;
        color: white;
    }
    button:hover {
        background-color: white;
        color: #03195a;
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
    .suggestions {
    cursor: pointer
    }
    .suggestions:hover {
        background-color: #f4aa09;
        border-radius: 5px;
    }
    .suggestions-container {
        position: absolute;
        background-color: #017754;
        border-radius: 10px 10px 10px 10px;
        align-items: left;
        display: flex;
        flex-direction: column;
        width: 200px;
        top: 173px;
        left: 43px;
    }
    .body {
        background-color: #03195a;
        color: white;
        height: 100vh;
        background-repeat: no-repeat;
        background-blend-mode: screen;
        background-size: cover;
        padding: 10px;
        }
</style>