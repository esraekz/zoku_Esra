// src/pages/invoices/uploaded.tsx
import React, { useState } from 'react';
import Head from 'next/head';
import InvoicesLayout from '../../components/Layout/InvoicesLayout';
import InvoiceList from '../../components/Invoices/InvoiceList';

const UploadedInvoicesPage: React.FC = () => {
  const [refreshKey] = useState<number>(0);

  return (
    <>
      <Head>
        <title>Uploaded Invoices | Zoku</title>
        <meta name="description" content="View your uploaded invoices" />
      </Head>

      <InvoicesLayout>
        <InvoiceList key={refreshKey} filterStatus="uploaded" />
      </InvoicesLayout>
    </>
  );
};

export default UploadedInvoicesPage;
