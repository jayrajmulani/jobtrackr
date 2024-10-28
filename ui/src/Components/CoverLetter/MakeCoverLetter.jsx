import React from 'react';
import { Button, Form, Input, message, Modal, Select } from 'antd';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import config from '../../config';

export default function MakeCoverLetter({ isOpen, onClose, updateCoverLetter }) {
    const [form] = Form.useForm();
    const { state } = useLocation();

    const closeForm = () => {
        form.resetFields();
        onClose();
    };

    const onOk = (values) => {
        axios
            .post(`${config.base_url}/generate_cv`, { ...values, email: state.email })
            .then(({ data }) => {
                message.success(data.message);
                updateCoverLetter(data.letter);
                closeForm();
            })
            .catch((err) => message.error(err.response.data?.error));
    };

    return (
        <Modal
            title="Make Cover Letter"
            open={isOpen}
            onCancel={closeForm}
            width={700}
            centered
            footer={[
                <Button onClick={closeForm} key="cancel" id="cancel">
                    Cancel
                </Button>,
                <Button type="primary" onClick={() => form.submit()} id="add-submit" key="ok">
                    Add
                </Button>,
            ]}
        >
            <Form form={form} layout="vertical" requiredMark={false} onFinish={onOk}>
                <Form.Item
                    label="Resume"
                    name="resume">
                    <Input placeholder="Input Resume Text" />
                </Form.Item>
                <Form.Item
                    label="Job Description"
                    name="job_desc"
                    rules={[
                        {
                            required: true,
                            message: 'Please input job description to tailor the Cover Letter!',
                        },
                    ]}
                >
                    <Input.TextArea placeholder="Job Description" />
                </Form.Item>
            </Form>
        </Modal>
    );
}
