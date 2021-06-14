<!-- 
    全局通用 css样式
-->

<template>
    <div id="testcss">
		<!-- button -->
		<div class="btn btn__primary"> <p>Button</p> </div>
		<div class="btn btn__secondary"> <p>Button</p> </div>

    </div>
</template>

<style>
/* TODO:VUE增加scss扩展
		使得 参数分离
			$a: #000000; //定义变量
			a {
				color:$a; //后面直接用，非常灵活
			}
*/
	vaule {
		--shadow: .3rem .3rem .6rem var(--greyLight-2), -.2rem -.2rem .5rem var(--white);
		--inner-shadow: inset .2rem .2rem .5rem var(--greyLight-2), inset -.2rem -.2rem .5rem var(--white);
	}

	/* button */

</style>