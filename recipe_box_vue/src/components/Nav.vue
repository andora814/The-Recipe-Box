<template>
  <nav>
    <router-link to="/" name="Home" class="nav-btn">Home</router-link>
    <router-link to="/recipebox" class="nav-btn">Recipe Box</router-link>
    <router-link to="/addrecipe" class="nav-btn">Add a Recipe</router-link>
    <router-link to="/about" class="nav-btn">About</router-link>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  data: () => ({
    categories: null
  })
};
</script>

<style scoped>
.nav-btn {
  cursor: pointer;
  text-decoration: none;
  color: grey;
}
.nav-btn:hover {
  color: white;
  font-weight: bolder;
}
.nav-btn {
  color: white
}
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: green;
}

</style>
