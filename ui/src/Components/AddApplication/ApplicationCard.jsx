import React from 'react';
import { Button, Card, Tag, Select } from 'antd';
import { EditFilled } from "@ant-design/icons";
import axios from 'axios';
import config from '../../config';
import { message } from 'antd';


function ApplicationCard({application, modalFunc, refresh, email}) {

    const columns = {
        "applied": "Applied",
        "inReview": "In Review",
        "interview": "Interview",
        "accepted": "Accepted",
        "rejected": "Rejected"
    }

    const quickUpdateApplications = (updatedValue) => {
        axios
        .post(`${config.base_url}/modify_application`, {
            companyName: application.companyName,
            jobTitle: application.jobTitle,
            jobId: application.jobId,
            description: application.description,
            url: application.url,
            date: application.date,
            status: updatedValue,
            image: application.image,
            _id: application._id,
            email: email,
        })
        .then(({ data }) => {
            message.success(data.message);
            refresh();
        })
        .catch((err) => message.error(err.response.data?.error))
    }

    return (
        <Card
            title={application.companyName}
            extra={
                <Button
                    type="text"
                    icon={<EditFilled />}
                    onClick={() => modalFunc(application)}
                    id={application.jobId + 'edit'}
                />
            }
            
            className="Job"
            bordered={false}
            actions={
                ['rejected', 'accepted'].includes(
                    application.status
                ) && [
                    application.status === 'accepted' ? (
                        <Tag color="#87d068">Accepted</Tag>
                    ) : (
                        application.status === 'rejected' && (
                            <Tag color="#f50">Rejected</Tag>
                        )
                    ),
                ]
            }
        >
            ID: {application.jobId}
            <br />
            Title: {application.jobTitle}
            <br />
            {'URL: '}
            <a href={'//' + application.url} target={'_blank'}>
                {application.url}
            </a>
            <br />
            Notes: {application.description}
            <br />
            Logo:
            <br />
            <img className="logo" src={application.image} />
            Quick Update:
            <br />
            <Select value={columns[application.status]} onChange={(value) => quickUpdateApplications(value)}>
                {
                    Object.keys(columns).map(
                        (col) => (
                            <Select.Option key={col} value={col}>
                                {columns[col]}
                            </Select.Option>
                            
                        )
                    )
                }
            </Select>
        </Card>
    );
};
export default ApplicationCard;