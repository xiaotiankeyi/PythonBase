#-*-coding:GBK -*-,
"""
mock ͨ��һ����˵����ģ��ӿڷ��ء�����ӿڵ�������ϵ��
��Ҫ��Ϊ�˽����Ԫ�����õĶ�
"""
def zhifu():
     """����������һ��֧���Ĺ���,δ������
     ֧���ɹ����أ�{"result": "success", "reason":"null"}
     ֧��ʧ�ܷ��أ�{"result": "fail", "reason":"����"}
     reason ����ʧ��ԭ��
     """
     pass

def zhifu_statues():
    '''����֧���Ľ�� success or fail���ж���ת����Ӧҳ��'''
    result = zhifu()
    print(result)
    try:
        if result["result"] == "success":
            return "֧���ɹ�"
        elif result["result"] == "fail":
            print("ʧ��ԭ��%s" % result["reason"])
            return "֧��ʧ��"
        else:
            return "δ֪�����쳣"
    except:
            return "Error, ����˷����쳣!"