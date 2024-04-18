import { useState, useEffect } from 'react'
import PositionsList from './PositionsList'
import AddStockForm from './AddStockForm'

const Portfolio = () => {

    const [positions, setPositions] = useState([])
    const [isModalOpen, setIsModalOpen] = useState(false)

    useEffect(() => {
        fetchPositions()
    }, [])

    const fetchPositions = async () => {
        const response = await fetch("http://127.0.0.1:5000/portfolio");
        const data = await response.json();
        setPositions(data.positions);
      };

    const closeModal = () => {
        setIsModalOpen(false)
    }

    const openCreateModal =() => {
        if (!isModalOpen) setIsModalOpen(true)
    }

    const onUpdate = () => {
        closeModal()
        fetchPositions()
    }

    return (
        <div className='portfolio'>
            <PositionsList positions={positions} updateCallback={onUpdate} />
            <button onClick={openCreateModal} className='button'>
                Add New Stock
            </button>
            { isModalOpen && <div className='modal'>
                <div className='modal-content'>
                    <span className='close' onClick={closeModal}>&times;</span>
                    <AddStockForm />
                </div>
            </div>
            }
        </div>
    );
}
 
export default Portfolio;