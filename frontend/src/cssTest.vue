<!-- 
    全局通用 css样式
		测试在 http://127.0.0.1:8080/testCss
-->

<template>
    <div id="testcss">
		CSS test
		<SearchBox/>
		<hr>
		<PointRun/>
		<br><br>
		<hr>

		<!-- button -->
		<div class="global_btn btn__primary"> <p>Button</p> </div>
		<hr>
		<div class="global_btn btn__secondary"> <p>Button</p> </div>

    </div>
</template>

<script>
    import SearchBox from '@/components/SearchBox.vue'
    import PointRun from '@/components//others/PointRun.vue'

	export default {
		name: 'gloCss',
		components:{
            SearchBox,
            PointRun,
        },
	}
</script>

<style>

</style>
