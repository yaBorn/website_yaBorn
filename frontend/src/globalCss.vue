<!-- 
    全局通用 css样式
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
		<div class="btn btn__primary"> <p>Button</p> </div>
		<hr>
		<div class="btn btn__secondary"> <p>Button</p> </div>

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
		data() {
			return {
				/* 用于 CSS的 Vue参数 参数分离方便调参 
					css中使用 v-bind(*) 详见BlogFooter.vue描述
					https://github.com/vuejs/rfcs/pull/231 */
				/* button */
				button:{
					// 大小
					width: '10rem',
					height: '4rem',
					texSize: '1.6rem',
					// 颜色
					color: 'rgb(43, 90, 151)', 		// 按钮颜色
					tex: 'rgb(232, 239, 248)', 		// 深按钮 字体颜色
					tex2: 'rgb(92, 149, 230)', 		// 浅按钮 字体颜色
					hightLight: 'rgb(121, 166, 230)', 	// 按钮 高光
					dark: 'rgb(31, 64, 109)', 		// 按钮 暗部
					topShadow: 'rgb(255, 255, 255)', 	// 上边框 阴影
					belowShadow: 'rgb(208, 214, 231)', // 下边框 阴影
				}
			}
		}
	}
</script>


<style>
	/* 颜色测试区 */
	colorTest {
		/* button */
			color: rgb(43, 90, 151); 		/* 按钮颜色 */
			tex: rgb(232, 239, 248);			/* 深按钮 字体颜色 */
			tex2: rgb(92, 149, 230);			/* 浅按钮 字体颜色 */
			hightLight: rgb(121, 166, 230); 	/* 按钮 高光 */
			dark: rgb(31, 64, 109);			/* 按钮 暗部 */
			topShadow: rgb(255, 255, 255);		/* 上边框 阴影 */
			belowShadow: rgb(208, 214, 231); 	/* 下边框 阴影 */
	}
	/* button */
	.btn {
		width: v-bind('button.width');
		height: v-bind('button.height');
		border-radius: 1rem;  /* 圆角大小 */
		box-shadow: 
			0.3rem 0.3rem 0.6rem v-bind('button.belowShadow'), 
			-0.2rem -0.2rem 0.5rem v-bind('button.topShadow');
		justify-self: center;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: pointer;
		transition: 0.3s ease;
	}
	.btn__primary {
		grid-column: 1/2;
		grid-row: 4/5;
		background: v-bind('button.color');
		box-shadow: 
			inset 0.2rem 0.2rem 1rem v-bind('button.hightLight'),
			inset -0.2rem -0.2rem 1rem v-bind('button.dark'), 
			0.3rem 0.3rem 0.6rem v-bind('button.belowShadow'), 
			-0.2rem -0.2rem 0.5rem v-bind('button.topShadow');
		color: v-bind('button.tex');
	}
	.btn__primary:hover {
		color: v-bind('button.topShadow');
	}
	.btn__primary:active {
		box-shadow: 
			inset 0.2rem 0.2rem 1rem v-bind('button.dark'), 
			inset -0.2rem -0.2rem 1rem v-bind('button.hightLight');
	}
	.btn__secondary {
		grid-column: 1/2;
		grid-row: 5/6;
		color: v-bind('button.tex2');
	}
	.btn__secondary:hover {
		color: v-bind('button.color');
	}
	.btn__secondary:active {
		box-shadow: 
			inset 0.2rem 0.2rem 0.5rem v-bind('button.belowShadow'), 
			inset -0.2rem -0.2rem 0.5rem v-bind('button.topShadow');
	}
	.btn p {
		font-size: v-bind('button.texSize');
	}
</style>
