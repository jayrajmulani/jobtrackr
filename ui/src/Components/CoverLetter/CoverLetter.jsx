import React, { useEffect, useState } from 'react';
import { EditOutlined, PlusOutlined } from '@ant-design/icons';
import { Button, Card, Empty } from 'antd';
import './Coverletter.scss'
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import config from '../../config';

export default function Coverletter() {
	const [loading, setLoading] = useState(true);
	const { state } = useLocation();

	useEffect(() => {
		updateCoverLetter();
	}, []);
	const updateCoverLetter = () => {
		
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
					>
						Generate Cover Letter
					</Button>
				</div>
			</div>
		</div>
	);

}
