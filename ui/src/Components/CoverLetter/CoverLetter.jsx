import React, { useEffect, useState } from 'react';
import { EditOutlined, PlusOutlined } from '@ant-design/icons';
import { Button, Card, Empty } from 'antd';
import './Coverletter.scss'
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import config from '../../config';
import MakeCoverLetter from './MakeCoverLetter';

export default function Coverletter() {
    const [coverLetter, setCoverLetter] = useState("");
    const [makeCoverLetterOpen, setCoverLetterOpen] = useState(false);
	const [loading, setLoading] = useState(true);
	const { state } = useLocation();

	useEffect(() => {
		updateCoverLetter();
	}, []);
	const updateCoverLetter = (letter) => {
		setCoverLetter(letter);
	}
    const toggleMakeCoverLetter = () => setMakeCoverletterOpen(!makeCoverLetterOpen);

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

                    />
				</div>
            </div>
		</div>
	);

}
