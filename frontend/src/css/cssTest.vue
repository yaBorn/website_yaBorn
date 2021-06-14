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

		<!-- 动画 -->
		<hr>
		<div class="global_anitest"></div>
		
		<!-- 分类 -->
		<hr>
		<div class="segmented-control">
			<input type="radio" name="radio2" value="3" id="tab-1" checked/>
				<label for="tab-1" class= "segmented-control__1">
					<p>Tab 1</p>
				</label>
			
			<input type="radio" name="radio2" value="4" id="tab-2" />
				<label for="tab-2" class= "segmented-control__2">
					<p>Tab 2</p>
				</label>
			
			<input type="radio" name="radio2" value="5" id="tab-3" />
				<label for="tab-3" class= "segmented-control__3">
					<p>Tab 3</p>
				</label>
							
			<div class="segmented-control__color"></div>
		</div>
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
