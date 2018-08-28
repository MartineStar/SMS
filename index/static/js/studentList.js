/*学生列表模块*/
function show_studentList(){//调用方法，传进json参数
	$('#grid').datagrid({
		//定义工具栏
		toolbar:[					
			{id:'add',text:'添加',iconCls:'icon-add',width:'100px',handler:function(){						
				if (editRow !== undefined) {
				   $('#grid').datagrid("endEdit", editRow);
				   editRow = undefined
				}
			   //添加时如果没有正在编辑的行，则在datagrid的第一行插入一行
				if (editRow === undefined) {
				  $('#grid').datagrid("insertRow", {
					   index: 0, // index start with 0
					   row: {}							//row:{} 表示插入一个空白行
				   });
				   //将新插入的那一行开户编辑状态
				   $('#grid').datagrid("beginEdit", 0);
				   //给当前编辑的行赋值
				   editRow = 0;
				}			
			}},
			{id:'remove',text:'删除',iconCls:'icon-remove',width:'100px',handler:function(){
				alert('删除信息')
			}},
			{id:'search',text:'查询',iconCls:'icon-search',width:'100px',handler:function(){
				alert('查询信息')
			}},
			//提交数据到服务器
			{id:'save',text:'提交',iconCls:'icon-save',width:'100px',handler:function(){
				var rows = $("#grid").datagrid("getRows");	//获取所有表格数据的json格式
				console.log(rows)
				$.ajax({
					url: 'xxxxxx', 
					data: rows,
					type: 'POST',
					dataType:'json',
					success: function (data) {
						console.log(data)
						//根据服务器返回的内容打印提交状况
						//alert('提交成功/失败')
					},
					error:function(error){
						console.log(error)
					}
				});
			}},		
			//撤销一切操作
			{id:'cancel',text:'取消',iconCls:'icon-cancel',width:'100px',handler:function(){
					//取消当前编辑行把当前编辑行罢undefined回滚改变的数据,取消选择的行
					editRow = undefined;
					$('#grid').datagrid("rejectChanges");
					$('#grid').datagrid("unselectAll");
			}}, 
			//导出到excel表格
			{id:'print',text:'导出excel',iconCls:'icon-print',width:'100px',handler:function(){
				alert('该模块暂时不可用，小哥哥正在努力实现呦...')
			}}, 
		],
		//表头(列信息)
		columns:[[
			{field:'code',title:'编号',width:200,
				editor:{					//步骤1，添加编辑器属性
					type:'validatebox',		//编辑器类型
					options:{			//编辑器属性
						required:true
					}
				}	
			},
			{field:'name',title:'商品名称',width:200,
				editor:{					//步骤1，添加编辑器属性
					type:'validatebox',		//编辑器类型
					options:{			//编辑器属性
						required:true
					}
				}
			},
			{field:'price',title:'商品价格',width:200,
				editor:{					//步骤1，添加编辑器属性
					type:'validatebox',		//编辑器类型
					options:{			//编辑器属性
						required:true
					}
				}}
		]],
		//远程数据
		//url:'data.json',		//ajax传输的json数据
		data:[
				{'code':'001','name':'笔记本','price':3000},
				{'code':'002','name':'手机','price':3050},
				{'code':'003','name':'自行车','price':300},
				{'code':'004','name':'耳机','price':90},
				{'code':'005','name':'键盘','price':300},
				{'code':'006','name':'空调','price':5000},	
				{'code':'001','name':'笔记本','price':3000},
				{'code':'002','name':'手机','price':3050},
				{'code':'003','name':'自行车','price':300},
				{'code':'004','name':'耳机','price':90},
				{'code':'005','name':'键盘','price':300},
				{'code':'006','name':'空调','price':5000},
				{'code':'001','name':'笔记本','price':3000},
				{'code':'002','name':'手机','price':3050},
				{'code':'003','name':'自行车','price':300},
				{'code':'004','name':'耳机','price':90},
				{'code':'005','name':'键盘','price':300},
				{'code':'006','name':'空调','price':5000},
			],
		//其他属性				
		rownumbers:true,		//显示行号
		pagination:true,		//显示分页条
		fit:true,
		onClickRow:function(rowIndex,rowData){			//单击选中，取消编辑					
			if (editRow !== undefined) {						
				$('#grid').datagrid("endEdit", editRow);
				editRow = undefined;
			}					 
		},
		//双击事件
		onDblClickRow:function(rowIndex,rowData){					
			if (editRow !== undefined) {
				$('#grid').datagrid("endEdit", editRow);
				editRow = undefined
			}
		   //添加时如果没有正在编辑的行，则在datagrid的第一行插入一行
			if (editRow === undefined) {					   
			   //将新插入的那一行开户编辑状态
				$('#grid').datagrid("beginEdit", rowIndex);
				//给当前编辑的行赋值
				editRow = rowIndex;
			}					
		},		//双击编辑行信息
		//pageList:[10],		//设置每页可显示多少条			
	})


}
