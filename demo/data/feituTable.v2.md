### **FeituTable 组件简要说明**

`FeituTable` 提供了丰富的配置项，允许用户自定义表格行为和样式。

#### **属性简要说明**：

- **`operations`**
  右上角操作按钮，如新增、批量删除等。

  ```tsx
  <FeituTable operations={[<Button>操作</Button>]} columns={[]} />
  ```

- **`prefixCls`**
  自定义样式前缀。

  ```tsx
  <FeituTable prefixCls="feitu-table-v2" columns={[]} />
  ```

- **`desName`**
  设置表格标题。

  ```tsx
  <FeituTable desName="数据表格" columns={[]} />
  ```

- **`hideTitle`**
  控制是否隐藏标题。

  ```tsx
  <FeituTable hideTitle={true} columns={[]} />
  ```

- **`hideTitleDetail`**
  控制是否隐藏标题详情。

  ```tsx
  <FeituTable hideTitleDetail={true} columns={[]} />
  ```

- **`hideTop`**
  控制是否隐藏顶部区域。

  ```tsx
  <FeituTable hideTop={true} columns={[]} />
  ```

- **`canEditColumns`**
  控制是否启用可编辑列。

  ```tsx
  <FeituTable canEditColumns={true} columns={[]} />
  ```

- **`editColumnsProps`**
  可编辑列的自定义属性。

  ```tsx
  <FeituTable canEditColumns={true} editColumnsProps={{ customProp: true }} columns={[]} />
  ```

- **`extraColumns`**
  额外的列，如操作列。

  ```tsx
  <FeituTable extraColumns={[{ title: '操作', dataIndex: 'action' }]} columns={[]} />
  ```

- **`columns`**
  定义表格的列。

  ```tsx
  <FeituTable columns={[{ title: '姓名', dataIndex: 'name' }]} />
  ```

- **`onFeituClearAll`**
  清空所有选中项时触发的回调。

  ```tsx
  <FeituTable onFeituClearAll={() => console.log('清空')} columns={[]} />
  ```

- **`autoPager`**
  控制是否启用自动分页。

  ```tsx
  <FeituTable autoPager={true} columns={[]} />
  ```

- **`dataSource`**
  表格的数据源。

  ```tsx
  <FeituTable dataSource={[{ key: '1', name: '张三' }]} columns={[]} />
  ```

- **`pagination`**
  配置分页器。

  ```tsx
  <FeituTable pagination={{ current: 1, pageSize: 10, total: 100 }} columns={[]} />
  ```