import React, { useEffect, useState } from 'react';
import { EditOutlined, PlusOutlined, DownloadOutlined } from '@ant-design/icons';
import { Button, Card, Empty } from 'antd';
import './Coverletter.scss'
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import config from '../../config';
import MakeCoverLetter from './MakeCoverLetter';

export default function Coverletter() {
    const [coverLetter, setCoverLetter] = useState("");
    const [makeCoverLetterOpen, setCoverLetterOpen] = useState(false);
	const { state } = useLocation();

	useEffect(() => {
		updateCoverLetter("");
	}, []);
	const updateCoverLetter = (letter) => {
		setCoverLetter(letter);
	}
    const toggleMakeCoverLetter = () => setCoverLetterOpen(!makeCoverLetterOpen);
	const downloadCoverLetter = () => {
		const url = window.URL.createObjectURL(new Blob([coverLetter], {type: 'text/plain'}));
			const link = document.createElement('a');
			link.href = url;
			link.setAttribute('download', "cv.txt");
			document.body.appendChild(link);
			link.click();
			document.body.removeChild(link);
	}
	return (
		<div className="CoverLetter">
			<div className="SubHeader">
				<div className="flex" />
				<div className="SubHeader">
					<div className="flex" />
					<Button
						id="generate-cv"
						type="primary"
						size="large"
						icon={<PlusOutlined />}
                        onClick={toggleMakeCoverLetter}
					>
						Generate Cover Letter
					</Button>
                    <MakeCoverLetter
                        isOpen={makeCoverLetterOpen}
                        onClose={toggleMakeCoverLetter}
                        updateCoverLetter={updateCoverLetter}
                    />
				</div>
            </div>
            <div className="CV">
                <Card className="CVCard" key={1} title={"Cover Letter"}>
                    {coverLetter}
										{coverLetter.length > 0 &&
										<>
										<br /> 
										<Button
											id="download"
											type="primary"
											size="large"
											icon={<DownloadOutlined />}
											onClick={downloadCoverLetter}
										>
											Download
										</Button>
										</>}
                </Card>
			</div>
		</div>
	);

}
