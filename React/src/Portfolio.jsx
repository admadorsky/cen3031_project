import { useState, useEffect } from 'react'
import PositionsList from './PositionsList'
import AddStockForm from './AddStockForm'

const Portfolio = () => {

    const [positions, setPositions] = useState([])
    const [isModalOpen, setIsModalOpen] = useState(false)
    const [currentPosition, setCurrentPosition] = useState({})

    useEffect(() => {
        fetchPositions()
    }, [])

    const fetchPositions = async () => {
        const response = await fetch("http://127.0.0.1:5000/portfolio");
        const data = await response.json();
        setPositions(data.positions);
        console.log(data.positions)
      };

    const closeModal = () => {
        setIsModalOpen(false)
        setCurrentPosition({})
    }

    const openCreateModal =() => {
        if (!isModalOpen) setIsModalOpen(true)
    }

    const openEditModal = (position) => {
        if (isModalOpen) return
        setCurrentPosition(position)
        setIsModalOpen(true)
    }

    const onUpdate = () => {
        closeModal()
        fetchPositions()
    }

    console.log(positions)

    return (
        <div className='portfolio'>
            <PositionsList positions={positions} updatePosition={openEditModal} updateCallback={onUpdate} />
            <button onClick={openCreateModal} className='button'>
                Add New Stock
            </button>
            { isModalOpen && <div className='modal'>
                <div className='modal-content'>
                    <span className='close' onClick={closeModal}>&times;</span>
                    <AddStockForm existingPosition={currentPosition} updateCallback={onUpdate}/>
                </div>
            </div>
            }
        </div>
    );
}
 
export default Portfolio;