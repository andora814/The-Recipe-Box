<template>
  <div class="recipe_container">
    <div class="container">
      <div @click="selectRecipe()">
        <h3> {{ recipe.title }} </h3>
        <img :src="recipe.image" alt="recipe picture" class="image" />
      </div>
      <div @click="deleteRecipe(recipe.id)" class="delBtn">remove</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecipeCard',
  data: () => ({
    showName: false,
    picclass: 'normal'
  }),
  props: {
    recipe: Object
  },
  methods: {
    async deleteRecipe(id) {
        await axios.delete(`http://localhost:8000/recipes/${id}`, {
          auth: {
            username: 'recipeboxuser',
            password: 'recipe'
          }
        })
        this.$emit('handleDelete', this.recipe.id)
    },
    selectRecipe(){
      this.$emit('click')
    }
}
}
</script>

<style scoped>

.container {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.center {
  position: absolute;
  top: 50%;
  text-align: center;
  font-size: 22px;
  color: black
}

.image  {
  height: 125px
  }

.blur {
  opacity: 0.6;
}

.recipe_container {
  cursor: pointer;
  background-color: white;
  background-image:
    linear-gradient(180deg, white 3rem, #f4aa09 calc(3rem), #f4aa09 calc(3rem + 2px), transparent 1px),
    repeating-linear-gradient(0deg, transparent, transparent 1.5rem, #DDD 1px, #DDD calc(1.5rem + 1px));
  box-shadow: 1px 1px 3px rgba(0,0,0,.25);
  height: 14rem;
  width: 400px;
  color: #017754;
  margin: 10px;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}

.recipe_container:hover {
  border-style: solid;
  border-color: #f4aa09;
}

.delBtn {
  width: 100%;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
}

.delBtn:hover {
  background-color: #f4aa09;
  color: #03195a;
  font-weight: bolder;
}

</style>