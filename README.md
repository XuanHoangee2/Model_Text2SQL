1. Giới thiệu

Project này fine-tune một mô hình LLM bằng QLoRA để thực hiện nhiệm vụ:
Natural Language → SQL (dựa trên dataset "chrisjcc/text-to-sql-spider-dataset") - Mục tiêu: xây dựng một internal AI assistant đa năng hỗ trợ truy vấn dữ liệu và trả lời câu hỏi nghiệp vụ.

2. Data Processing

Sau khi tải bộ dataset về chúng ta sẽ loại bỏ những dữ liệu khuyết cũng như phân thành các bộ dataset phù hợp với mục đích sử dụng của bản thân
