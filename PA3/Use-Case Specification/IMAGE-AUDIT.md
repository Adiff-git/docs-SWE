# Rà soát hình ảnh Use-Case Specifications

Phạm vi: 56 tài liệu đã tải từ Thịnh, Gia, Thành 1 và Kiên; không gồm Nháp. Kiểm tra ảnh nhúng của Markdown, đối chiếu số hình lớn trong PDF, xem các ảnh prototype và render các trang có dấu hiệu bị cắt. Đây là tình trạng của bản tải về, chưa kiểm tra các chỉnh sửa Google Docs sau thời điểm tải.

Phân loại dựa trên hình minh họa luồng chính, kết quả thao tác và nhánh thay thế tiêu biểu. Không mặc định rằng mọi lỗi kỹ thuật phải có một hình riêng. Những mục “nên bổ sung” là nhận định về độ bao phủ, không phải lỗi thiếu file ảnh.

Kết quả: 7 tài liệu không có hình; 19 tài liệu có hình nhưng còn thiếu nội dung/thao tác chính hoặc bị cắt; 10 tài liệu nên bổ sung hình cho nhánh thay thế. Các mục không liệt kê không đồng nghĩa đã bao phủ mọi alternative flow.

## 1. Chưa có hình

| Use case | Hình hiện có | Nhận xét |
| --- | ---: | --- |
| [UC-011 — Delete Account](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-02 -- Profile Management/FG-02 -- 011 -- Delete Account.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |
| [UC-016 — Compare Products](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 016 -- Compare Products.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |
| [UC-018 — View Recently Viewed Products](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 018 -- View Recently Viewed Products.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |
| [UC-020 — View Personalized Recommendations](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 020 -- View Personalized Recommendations.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |
| [UC-021 — Manage Recommendation Preferences](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 021 -- Manage Recommendation Preferences.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |
| [UC-022 — Manage Wishlist](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 022 -- Manage Wishlist.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |
| [UC-023 — Manage Shopping Cart](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-04 -- Shopping Cart/FG-04 -- 023 -- Manage Shopping Cart.pdf>) | 0 | Chưa có hình prototype trong cả Markdown và PDF. |

## 2. Có hình nhưng chưa đầy đủ

| Use case | Hình hiện có | Nhận xét |
| --- | ---: | --- |
| [UC-004 — Verify Email](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-01 -- Authentication/FG-01 -- 004 -- Verify Email.pdf>) | 1 | Chỉ có màn hình chờ email; thiếu kết quả xác minh thành công/thất bại và trạng thái gửi lại. |
| [UC-006 — Change Password](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-01 -- Authentication/FG-01 -- 006 -- Change Password.pdf>) | 1 | Chỉ có form đổi mật khẩu; thiếu kết quả thành công/yêu cầu đăng nhập lại và lỗi mật khẩu hiện tại hoặc xác nhận. |
| [UC-007 — Login with Google](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-01 -- Authentication/FG-01 -- 007 -- Login with Google.pdf>) | 1 | Chỉ có nút Google trên trang đăng nhập; thiếu bước phía Google, kết quả quay về ứng dụng và trường hợp hủy/trùng tài khoản. |
| [UC-009 — Manage Profile](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-02 -- Profile Management/FG-02 -- 009 -- Manage Profile.pdf>) | 4 | Có profile và đổi email, nhưng chính Scope ghi thiếu giao diện xóa avatar và đặt mật khẩu ban đầu. |
| [UC-015 — View Product Details](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 015 -- View Product Details.pdf>) | 3 | Figure 2, PDF trang 8, cắt mất phần đầu bảng thông số; phần lớn hình là đánh giá. Cần ảnh thông số đầy đủ; chưa có trạng thái biến thể hết hàng/không khả dụng. |
| [UC-017 — View Product Promotions](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 017 -- View Product Promotions.pdf>) | 2 | Chỉ có badge/giá giảm và nhãn quà tặng; thiếu thông tin điều kiện/phạm vi khuyến mãi đầy đủ và trạng thái không còn áp dụng. Scope cũng ghi thiếu promotion-terms view. |
| [UC-027 — Make Payment](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-05 -- Checkout & Payment/FG-05 -- 027 -- Make Payment.pdf>) | 2 | Có chọn COD và đơn chưa thanh toán; thiếu minh họa xác nhận thu tiền/kết quả đã thanh toán. Online payment chỉ cần nếu nhóm duyệt phạm vi đó. |
| [UC-028 — View Payment Status](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-05 -- Checkout & Payment/FG-05 -- 028 -- View Payment Status.pdf>) | 2 | Ảnh thể hiện COD chưa thanh toán và một trạng thái đơn đã giao; chưa minh họa rõ đầy đủ số tiền, paid-at và trạng thái thanh toán khác. Trạng thái giao hàng không thay thế trạng thái thanh toán. |
| [UC-031 — Manage Products](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 031 -- Manage Products.pdf>) | 2 | Có danh sách và xác nhận xóa sản phẩm; thiếu form tạo/sửa và kết quả lưu tương ứng với basic flow. |
| [UC-034 — Manage Product Variants & Prices](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 034 -- Manage Product Variants & Prices.pdf>) | 2 | Dùng chung ảnh form sản phẩm với UC-035/036; thiếu màn hình tập trung quản lý biến thể/giá, thao tác sửa và lỗi cụ thể. Ảnh trạng thái chung không chứng minh các bước này. |
| [UC-035 — Manage Product Images](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 035 -- Manage Product Images.pdf>) | 2 | Có vùng ảnh trong form sản phẩm chung; thiếu trạng thái upload, xóa/sắp xếp/chọn ảnh chính và lỗi định dạng/dung lượng theo flow. |
| [UC-036 — Manage Product Specifications](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 036 -- Manage Product Specifications.pdf>) | 2 | Có vùng thông số trong form sản phẩm chung nhưng thiếu thao tác sửa key/value/đơn vị và lỗi thuộc tính trùng/không hợp lệ. |
| [UC-037 — Manage Product Stock](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 037 -- Manage Product Stock.pdf>) | 2 | Chỉ có danh sách sản phẩm và bộ trạng thái chung; thiếu form điều chỉnh tồn theo biến thể, số lượng reserved/available, kết quả điều chỉnh và xung đột tồn kho. |
| [UC-042 — Request Return](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-07 -- Order Management/FG-07 -- 042 -- Request Return.pdf>) | 2 | PDF trang 6 bị cắt đáy form/nút gửi; chưa có màn hình xác nhận đã gửi kèm mã yêu cầu và trạng thái thực tế. |
| [UC-043 — Request Refund](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-07 -- Order Management/FG-07 -- 043 -- Request Refund.pdf>) | 2 | Ảnh form bị cắt đáy tương tự UC-042; thiếu kết quả gửi yêu cầu hoàn tiền kèm mã/trạng thái. |
| [UC-047 — Manage Store Settings & Homepage Content](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-09 -- Store Administration/FG-09 -- 047 -- Manage Store Settings & Homepage Content.pdf>) | 1 | Chỉ có ảnh homepage phía khách hàng. Thiếu hoàn toàn giao diện admin chỉnh settings/banner/nội dung và Save/Publish; Scope xác nhận ảnh chỉ làm bối cảnh. |
| [UC-056 — Manage Shopping Cart via AI](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-10 -- AI Chatbot & Shopping Automation/FG-10 -- 056 -- Manage Shopping Cart via AI.pdf>) | 2 | Có preview và thiếu hàng; thiếu bước khách xác nhận thay đổi cùng kết quả giỏ hàng đã cập nhật như basic flow. Tài liệu đánh dấu later-phase concept. |
| [UC-057 — Prepare Checkout via AI](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-10 -- AI Chatbot & Shopping Automation/FG-10 -- 057 -- Prepare Checkout via AI.pdf>) | 2 | Có chat chuyển sang checkout; thiếu minh họa trang checkout được mở với đúng các món và dữ liệu cần rà soát. Có thể tham chiếu rõ UC-025 thay vì lặp hình. Tài liệu đánh dấu later-phase concept. |
| [UC-059 — Manage AI Conversation History](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-10 -- AI Chatbot & Shopping Automation/FG-10 -- 059 -- Manage AI Conversation History.pdf>) | 2 | Có thẻ mở hội thoại và empty state; thiếu danh sách tiêu đề/ngày cập nhật, transcript sau khi mở lại, xác nhận xóa và danh sách sau xóa. |

## 3. Nên bổ sung hình nhánh thay thế

| Use case | Hình hiện có | Nhận xét |
| --- | ---: | --- |
| [UC-001 — Register Account](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-01 -- Authentication/FG-01 -- 001 -- Register Account.pdf>) | 2 | Có form đăng ký/check-email; thiếu hình lỗi email đã dùng, mật khẩu không khớp hoặc validation đại diện. |
| [UC-012 — Browse Product Catalog](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 012 -- Browse Product Catalog.pdf>) | 3 | Có các màn hình duyệt danh mục; thiếu danh mục rỗng hoặc không khả dụng. |
| [UC-019 — View Homepage Recommendations](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-03 -- Search And Browse/FG-03 -- 019 -- View Homepage Recommendations.pdf>) | 1 | Có featured products; thiếu trạng thái không có gợi ý/cấu hình không hợp lệ. |
| [UC-030 — View Product Sales Overview](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 030 -- View Product Sales Overview.pdf>) | 2 | Ảnh thay thế là bộ trạng thái quản lý sản phẩm chung; cần trạng thái không có dữ liệu báo cáo/khoảng thời gian sai hoặc lỗi tải thống kê. |
| [UC-032 — Manage Product Categories](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 032 -- Manage Product Categories.pdf>) | 2 | Dùng bộ trạng thái sản phẩm chung; cần lỗi trùng danh mục/xóa danh mục đang được dùng theo flow. |
| [UC-033 — Manage Product Brands](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-06 -- Product Management/FG-06 -- 033 -- Manage Product Brands.pdf>) | 2 | Dùng bộ trạng thái sản phẩm chung; cần lỗi trùng thương hiệu hoặc thương hiệu đang được tham chiếu. |
| [UC-045 — View Product Reviews & Ratings](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-08 -- Review & Rating/FG-08 -- 045 -- View Product Reviews & Ratings.pdf>) | 1 | Chỉ có danh sách đánh giá; Scope ghi thiếu phân trang, chưa có đánh giá và lỗi dịch vụ. |
| [UC-046 — Manage Product Reviews & Ratings](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-08 -- Review & Rating/FG-08 -- 046 -- Manage Product Reviews & Ratings.pdf>) | 3 | Có form và xác nhận gửi; thiếu validation rating/nội dung/upload hoặc không đủ điều kiện. Edit/delete chỉ cần khi nhóm chốt thêm phạm vi đó. |
| [UC-049 — Manage Promotions & Vouchers](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-09 -- Store Administration/FG-09 -- 049 -- Manage Promotions & Vouchers.pdf>) | 2 | Có danh sách/form; thiếu mã trùng, ngày không hợp lệ hoặc giới hạn khuyến mãi không hợp lệ. |
| [UC-051 — View Sales Statistics](<C:/Users/TrinhThanh/Downloads/docs-SWE/PA3/Use-Case Specification/FG-09 -- Store Administration/FG-09 -- 051 -- View Sales Statistics.pdf>) | 1 | Chỉ có dashboard có dữ liệu; thiếu báo cáo rỗng, khoảng ngày sai hoặc lỗi xuất báo cáo. Scope ghi chưa có empty/error frame. |

## UC-024 chưa có tài liệu riêng

UC-024 — Apply Discount Code trong tab Kiên trỏ cùng URL với UC-023. Vì vậy chưa có specification/hình riêng của UC-024 để đánh giá. File UC-023 hiện không có hình và ghi voucher áp dụng ở checkout; không thể coi đó là minh họa đầy đủ cho UC-024.

Ưu tiên: bổ sung 7 file chưa có hình và UC-024; tiếp theo UC-047, UC-037, UC-004, UC-007, UC-027, UC-059; sau đó sửa ảnh cắt của UC-015/042/043 và các nhánh thay thế.
