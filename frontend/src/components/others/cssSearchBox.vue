<!-- 
    搜索框 css 测试
-->

<!-- js -->
<script>
    export default {
        name: 'PointRun',
    }    
</script>

<!-- html -->
<template>
	<div class="container">
		<div class="search">
			<input type="text" class="search__input" placeholder="Search...">
			<div class="search__icon">
				<ion-icon name="search">
				</ion-icon>
			</div>
		</div>
    </div>
</template>

<!-- css -->
<style scoped>
	:root {
		--searchIco1: #8d8d8d;
		--searchIco2: #3a3a3a;
		--shadowWhite: #FFFFFF;
		--shadowBlack: #c8d0e7;
		--background: #E4EBF5;
		--text: #7a7a7a;
	}
	@media screen and (min-width: 900px) {
		html {
			font-size: 75%;
		}
	}
	.container {
		min-height: 100vh;
		display: flex;
		justify-content: center;
		align-items: center;
		font-family: "Poppins", sans-serif;
		background: var(--background);
	}
	.search {
		grid-column: 3/4;
		grid-row: 2/3;
		position: relative;
		display: flex;
		align-items: center;
	}
	.search__input {
		width: 20.4rem;
		height: 4rem;
		border: none;
		border-radius: 1rem;
		font-size: 1.4rem;
		padding-left: 3.8rem;
		box-shadow: inset 0.2rem 0.2rem 0.5rem var(--shadowBlack), inset -0.2rem -0.2rem 0.5rem var(--shadowWhite);
		background: none;
		font-family: inherit;
		color: var(--searchIco1);
	}
	.search__input::-moz-placeholder {
		color: var(--text);
	}
	.search__input:-ms-input-placeholder {
		color: var(--text);
	}
	.search__input::placeholder {
		color: var(--text);
	}
	.search__input:focus {
		outline: none;
		box-shadow: 0.3rem 0.3rem 0.6rem var(--shadowBlack), -0.2rem -0.2rem 0.5rem var(--shadowWhite);
	}
	.search__input:focus + .search__icon {
		color: var(--searchIco2);
	}
	.search__icon {
		height: 2rem;
		position: absolute;
		font-size: 2rem;
		padding: 0 1rem;
		display: flex;
		color: var(--searchIco1);
		transition: 0.3s ease;
	}
</style>
