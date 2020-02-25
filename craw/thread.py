import threading
import time
from concurrent.futures import ThreadPoolExecutor
import json

def worker(thread):
    for i in range(100):
        print ("thread...."+str(thread)+"  :  "+str(i))
dict={
    "1": {
    },
    "2": [
        "Mình có việc đi xa nên đặt mua cái địu bế bé cho dễ. Vì lúc đặt hàng mình cứ nghĩ 2-3 ngày sau là có hàng ai dè nhìn kỹ thì cả tuần sau mới nhận được. Mình liền gọi hỏi Tiki ngay thì được bạn Thảo hỗ trợ dễ thương mà còn rất nhanh sau đó (1ngay sau) đã báo sẽ chuyển sớm cho mình rồi. Cám on bạn Thảo rất nhiều. Về sản phẩm - Đong gói của Tiki thì không phải bàn rồi. Sản phẩm đẹp, có hướng dẫn đầy đủ, y như giới thiệu trên trang web tiki. Mình cho 2 sao là vì mình vừa mua 1.620k hôm trước thì hôm nay Tiki lại giảm thêm 300k nữa. Buồn hết sức (((",
        "Mua địu này là một điều tiếc của mình:(( Địu đau vai lắm. Mà rất khó sử dụng. Khi địu chân con dạng ra rất nhiều sẽ có thể gây tật chân vòng kiềng. Mới mua dùng 1 lần chắc sẽ không dùng nữa quá:(",
        "Chất vải cứng, nóng, địu ra ngoài 1 lúc về là con bị đỏ mông. Nên mua loại có đệm đỡ ở bụng và loại vải mềm chắc sẽ ok hơn."
    ],
    "3": [
        "Mình nghiên cứu rồi đặt mua chứ chưa sử dụng liền nên chưa biết khi sử dụng sẽ như nào. Thời gian giao hàng khá chậm. Hàng giao như mô tả, đúng loại, đúng màu, nhìn dày dặn, chắc chắn. Nhưng có 1 điều rất bực mình là hàng tặng là 2 bich khăn giấy đã hết hạn sử dụng. Thà đừng tặng chứ tặng như này thì như là tặng rác cho khách hàng rồi. Trong hình có chụp dòng chữ ngày sx trên bao bì là 325a50501 và có hướng dẫn đọc ngày sx bằng tiếng việt thì theo hướng dẫn là 3 năm từ ngày 25/11/2015 trong khi giao hàng cho mình là gần cuối tháng 12/2018.",
        "Sản phẩm đóng gói kĩ càng, hàng mở ra k khác so với hình ảnh. Sản phẩm đúng tiêu chuẩn. Vải thô so với em bé. Đai cảm giác chắc chắn và an toàn",
        "Tôi nhận hàng rồi nhưng ko có nón như trên mô tả sản phẩm."
    ],
    "4": [
        "Hàng của Aprica thì khỏi chê về chất lượng. Địu đc nhiều tư thế, tiện dụng, màu sắc trang nhã, kiểu đang đẹp. Mua trên Tiki đc đóng gói cẩn thận, giao nhanh, lại đc giảm giá nhiều hơn những chỗ khác nữa. Từ khi có em địu này mình đưa bé ra ngoài chơi dễ dàng hơn hẳn!",
        "Địu đẹp giống hình . Mình tia em này lâu rồi nhưng còn phân vân vì giá cũng chát nên khi có đợt sale mình chớp ngay hihi . Trong 3 màu màu này đep nhất mà cũng dễ dơ nhất . Hãng nên thêm vài màu khác để các mẹ có thêm sự lựa chọn . Mình hài lòng ngay lần đầu sử dụng , bé có vẻ thích thú mà mẹ cũng nhàn hẳn , k phải ngó trước ngó sau khi chở bé bằng xe máy. Một sản phẩm đáng để sử dụng",
        "Đã nhận đai ngày 1/7/2016, tiki giao hàng rất nhanh, hàng về kho ngày 29/6 thì 2 ngày sau mình nhận được rồi dù trên web vẫn ghi dự kiến là 5/7 lận, mình rất vui. Đóng gói rất cẩn thận, sản phẩm màu tím rất đẹp và chắc chắn. Mình đặt mua đúng đợt giảm còn 1566k, hôm nay nhận hàng xong vào tiki lại thấy lên 1620k, đỡ quá đi!",
        "Mình mua đợt sale 499. Cảm nhận chất lượng khá ổn. Nhìn chỉ khâu và chất liệu cao cấp. Mỗi tội vợ mình không thích dùng. :v",
        "Mua vào đợt săn deal của Tiki, sản phẩm tương đối tốt, chắc vải bền, tuy nhiên phần vai hơi cứng một chút, nhưng vẫn chất lượng hơn so với hàng trôi nổi trên thị trường!",
        "Mua vào đợt giá giá còn 1390k. Khá hài lòng với nhãn hàng của Nhật này. Có 4 tư thế đeo nên khá thuận tiện. Tuy nhiên chất vải bên ngoài không được mềm lắm",
        "Sản phẩm đẹp, nhưng thời gian đợi giao hàng hơi lâu mặc dù mình thấy có dịch vụ tikinow khi giao hàng",
        "Cho mình hỏi địu mình mua được 4 tháng mà bị rớt mất nút cài phía sau, shop có hổ trợ bảo hành không ạ",
        "Mình mới nhận hàng nhưng do bé không vừa với địu, mịn có thể trả hàng không?"
    ],
    "5": [
        "Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc Tốtfcccdcccc",
        "Hàng của Nhật Bản, xài rất tốt, thông thoáng, mình kỹ tính nhưng phải nói rất hài lòng với sản phẩm này, con mình đặt vào ngủ ngon lành lắm, an toàn hơn bồng ẵm mà mình vẫn có thể làm việc khi cho con ngủ, rất khỏe. Khuyến nghị mua ngay cho bé từ 1 tháng tuổi.",
        "Mua đúng dịp sinh nhật Tiki nên giá quá thơm (499k). Hàng đúng như hình, chất liệu khá đẹp.Khá ưng ý với sản phẩm này, có cái bọc mang đi đâu cũng tiện.",
        "Vừa nhận được địu hôm qua, cảm giác rất hài lòng. Lớp đệm êm ái, không bí hơi, các đai chắc chắn. Có thể gấp gọn địu bỏ trong túi xách đi kèm Bé nằm trong địu rất thoải mái, không gò bó như các địu mình đã sử dụng Màu tím sạch, dẽ thương Mình mua dịp giảm giá nên với giá 1200k là quá rẻ cho 1 cái địu chất lượng Tiki đóng gói cẩn thận, giao hàng nhanh, thân thiện Sẽ tiếp tục ủng hộ Tiki :)",
        "Sản phẩm hoàn thiện tốt, đường mai đẹp chắc chắn, đóng gói cẩn thận có tem hàng dễ vỡ và giao hàng nhanh.",
        "Địu chắc chắn, đường chỉ may đẹp. Địu được nhiều tư thế.",
        "Giá tốt, an tâm mua sản phẩm này nhe mn, mình đã mua và cảm thấy ưng ý!",
        "Địu tốt, hàng chất lượng.. mình rất yên tâm khi mua hàng của tiki",
        "Hài lòng, sản phẩm đẹp, nhẹ. Bé rất thích...........",
        "Địu chắc chắn, màu tím nhẹ nhàng. Hộp hơi móp một chút.",
        "Sản phẩm đúng như hình hàng sử dụng tốt ủng hộ tiếp",
        "Máy đẹp, đóng gói cẩn thận Máy đẹp, đóng gói cẩn thận",
        "Sản phẩm giao đúng hình mẫu, giá tốt nhất thị trường.",
        "Đai chắc chắn. Giống y như hình. Xài ok lắm nhe!!!",
        "Sản phẩm đúng mô tả, Tiki giao hàng nhanh, đạt 5 sao",
        "Sản phẩm chất lượng tốt + với mua được trong đợt khuyến mãi nên giá khá mềm. Mới chỉ mở ra kiểm tra sơ bộ chưa sử dụng thử"
    ],
    "productId": 134146,
    "url": "https://tiki.vn/diu-tre-em-aprica-pitta-p134146.html?spid=25552547"
}

def encode():
     print(dict)
     print(json.dumps(dict))
encode()
# threads = []
# executor = ThreadPoolExecutor(max_workers=5)
#
# for i in range(5):
#
#     thread = threading.Thread(target=worker(i))
#     executor.submit(thread)