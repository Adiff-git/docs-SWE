from pathlib import Path
import json
rows=json.loads(Path('tmp/image-audit/audit.json').read_text(encoding='utf-8'))
missing={r['uc']:'Chưa có hình prototype trong cả Markdown và PDF.' for r in rows if r['images']==0}
partial={
'004':'Chỉ có màn hình chờ email; thiếu kết quả xác minh thành công/thất bại và trạng thái gửi lại.',
'006':'Chỉ có form đổi mật khẩu; thiếu kết quả thành công/yêu cầu đăng nhập lại và lỗi mật khẩu hiện tại hoặc xác nhận.',
'007':'Chỉ có nút Google trên trang đăng nhập; thiếu bước phía Google, kết quả quay về ứng dụng và trường hợp hủy/trùng tài khoản.',
'009':'Có profile và đổi email, nhưng chính Scope ghi thiếu giao diện xóa avatar và đặt mật khẩu ban đầu.',
'015':'Figure 2, PDF trang 8, cắt mất phần đầu bảng thông số; phần lớn hình là đánh giá. Cần ảnh thông số đầy đủ; chưa có trạng thái biến thể hết hàng/không khả dụng.',
'017':'Chỉ có badge/giá giảm và nhãn quà tặng; thiếu thông tin điều kiện/phạm vi khuyến mãi đầy đủ và trạng thái không còn áp dụng. Scope cũng ghi thiếu promotion-terms view.',
'027':'Có chọn COD và đơn chưa thanh toán; thiếu minh họa xác nhận thu tiền/kết quả đã thanh toán. Online payment chỉ cần nếu nhóm duyệt phạm vi đó.',
'028':'Ảnh thể hiện COD chưa thanh toán và một trạng thái đơn đã giao; chưa minh họa rõ đầy đủ số tiền, paid-at và trạng thái thanh toán khác. Trạng thái giao hàng không thay thế trạng thái thanh toán.',
'031':'Có danh sách và xác nhận xóa sản phẩm; thiếu form tạo/sửa và kết quả lưu tương ứng với basic flow.',
'034':'Dùng chung ảnh form sản phẩm với UC-035/036; thiếu màn hình tập trung quản lý biến thể/giá, thao tác sửa và lỗi cụ thể. Ảnh trạng thái chung không chứng minh các bước này.',
'035':'Có vùng ảnh trong form sản phẩm chung; thiếu trạng thái upload, xóa/sắp xếp/chọn ảnh chính và lỗi định dạng/dung lượng theo flow.',
'036':'Có vùng thông số trong form sản phẩm chung nhưng thiếu thao tác sửa key/value/đơn vị và lỗi thuộc tính trùng/không hợp lệ.',
'037':'Chỉ có danh sách sản phẩm và bộ trạng thái chung; thiếu form điều chỉnh tồn theo biến thể, số lượng reserved/available, kết quả điều chỉnh và xung đột tồn kho.',
'042':'PDF trang 6 bị cắt đáy form/nút gửi; chưa có màn hình xác nhận đã gửi kèm mã yêu cầu và trạng thái thực tế.',
'043':'Ảnh form bị cắt đáy tương tự UC-042; thiếu kết quả gửi yêu cầu hoàn tiền kèm mã/trạng thái.',
'047':'Chỉ có ảnh homepage phía khách hàng. Thiếu hoàn toàn giao diện admin chỉnh settings/banner/nội dung và Save/Publish; Scope xác nhận ảnh chỉ làm bối cảnh.',
'056':'Có preview và thiếu hàng; thiếu bước khách xác nhận thay đổi cùng kết quả giỏ hàng đã cập nhật như basic flow. Tài liệu đánh dấu later-phase concept.',
'057':'Có chat chuyển sang checkout; thiếu minh họa trang checkout được mở với đúng các món và dữ liệu cần rà soát. Có thể tham chiếu rõ UC-025 thay vì lặp hình. Tài liệu đánh dấu later-phase concept.',
'059':'Có thẻ mở hội thoại và empty state; thiếu danh sách tiêu đề/ngày cập nhật, transcript sau khi mở lại, xác nhận xóa và danh sách sau xóa.',
}
alternatives={
'001':'Có form đăng ký/check-email; thiếu hình lỗi email đã dùng, mật khẩu không khớp hoặc validation đại diện.',
'012':'Có các màn hình duyệt danh mục; thiếu danh mục rỗng hoặc không khả dụng.',
'019':'Có featured products; thiếu trạng thái không có gợi ý/cấu hình không hợp lệ.',
'030':'Ảnh thay thế là bộ trạng thái quản lý sản phẩm chung; cần trạng thái không có dữ liệu báo cáo/khoảng thời gian sai hoặc lỗi tải thống kê.',
'032':'Dùng bộ trạng thái sản phẩm chung; cần lỗi trùng danh mục/xóa danh mục đang được dùng theo flow.',
'033':'Dùng bộ trạng thái sản phẩm chung; cần lỗi trùng thương hiệu hoặc thương hiệu đang được tham chiếu.',
'045':'Chỉ có danh sách đánh giá; Scope ghi thiếu phân trang, chưa có đánh giá và lỗi dịch vụ.',
'046':'Có form và xác nhận gửi; thiếu validation rating/nội dung/upload hoặc không đủ điều kiện. Edit/delete chỉ cần khi nhóm chốt thêm phạm vi đó.',
'049':'Có danh sách/form; thiếu mã trùng, ngày không hợp lệ hoặc giới hạn khuyến mãi không hợp lệ.',
'051':'Chỉ có dashboard có dữ liệu; thiếu báo cáo rỗng, khoảng ngày sai hoặc lỗi xuất báo cáo. Scope ghi chưa có empty/error frame.',
}
out=['# Rà soát hình ảnh Use-Case Specifications','',
'Phạm vi: 56 tài liệu đã tải từ Thịnh, Gia, Thành 1 và Kiên; không gồm Nháp. Kiểm tra ảnh nhúng của Markdown, đối chiếu số hình lớn trong PDF, xem các ảnh prototype và render các trang có dấu hiệu bị cắt. Đây là tình trạng của bản tải về, chưa kiểm tra các chỉnh sửa Google Docs sau thời điểm tải.',
'', 'Phân loại dựa trên hình minh họa luồng chính, kết quả thao tác và nhánh thay thế tiêu biểu. Không mặc định rằng mọi lỗi kỹ thuật phải có một hình riêng. Những mục “nên bổ sung” là nhận định về độ bao phủ, không phải lỗi thiếu file ảnh.', '',
f'Kết quả: {len(missing)} tài liệu không có hình; {len(partial)} tài liệu có hình nhưng còn thiếu nội dung/thao tác chính hoặc bị cắt; {len(alternatives)} tài liệu nên bổ sung hình cho nhánh thay thế. Các mục không liệt kê không đồng nghĩa đã bao phủ mọi alternative flow.', '']
for title,mapping in [('1. Chưa có hình',missing),('2. Có hình nhưng chưa đầy đủ',partial),('3. Nên bổ sung hình nhánh thay thế',alternatives)]:
 out += ['## '+title,'','| Use case | Hình hiện có | Nhận xét |','| --- | ---: | --- |']
 for uc,why in mapping.items():
  r=next(x for x in rows if x['uc']==uc); label='UC-'+uc+' — '+r['name'].split(' -- ',2)[2]
  pdf=Path(r['path']).with_suffix('.pdf').as_posix()
  out.append(f'| [{label}](<{pdf}>) | {r["images"]} | {why} |')
 out.append('')
out+=['## UC-024 chưa có tài liệu riêng','', 'UC-024 — Apply Discount Code trong tab Kiên trỏ cùng URL với UC-023. Vì vậy chưa có specification/hình riêng của UC-024 để đánh giá. File UC-023 hiện không có hình và ghi voucher áp dụng ở checkout; không thể coi đó là minh họa đầy đủ cho UC-024.', '', 'Ưu tiên: bổ sung 7 file chưa có hình và UC-024; tiếp theo UC-047, UC-037, UC-004, UC-007, UC-027, UC-059; sau đó sửa ảnh cắt của UC-015/042/043 và các nhánh thay thế.']
Path('PA3/Use-Case Specification/IMAGE-AUDIT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print(len(missing),len(partial),len(alternatives))
