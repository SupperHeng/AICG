from Client import client
print('请问有什么能够帮助到您？\n')

# 初始化消息历史
messages_history = [
    {"role": "system", "content": "你是一个乐于助人的助手。"}
]

while True:
    # 获取用户输入
    user_input = input()

    # 结束对话的条件
    if user_input.lower() == '退出':
        print('对话结束，感谢您的使用！')
        break

    # 将用户输入添加到消息历史中
    messages_history.append({"role": "user", "content": user_input})

    # 调用模型获取回复
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages_history,
        stream=True,
    )

    # 处理模型回复的输出
    data_content = ""
    for chunk in response:
        data_content += chunk.choices[0].delta.content
        print(chunk.choices[0].delta.content, end='', flush=True)

    # 换行
    print()

    # 将模型的回复添加到消息历史中
    messages_history.append({"role": "assistant", "content": data_content})
