import React from 'react'
import { render, screen } from '@testing-library/react'
import { UserCard } from '../src/components/UserCard'

describe('UserCard Component', () => {
  const mockUser = {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com',
    active: true,
  }

  test('renders user information', () => {
    render(<UserCard user={mockUser} />)

    expect(screen.getByText('John Doe')).toBeInTheDocument()
    expect(screen.getByText('john@example.com')).toBeInTheDocument()
  })

  test('displays active status', () => {
    render(<UserCard user={mockUser} />)

    expect(screen.getByText('Active')).toBeInTheDocument()
  })

  test('displays inactive status when user is inactive', () => {
    const inactiveUser = { ...mockUser, active: false }

    render(<UserCard user={inactiveUser} />)

    expect(screen.getByText('Inactive')).toBeInTheDocument()
  })
})
